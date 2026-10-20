-- Offline practice using the four aggregates supplied in the interview case.
-- SQLite syntax. Each row represents one acquisition channel in one week.
-- Assumptions: mutually exclusive, exhaustive channels; comparable eligible
-- user cohorts; identical activation definitions and complete follow-up windows.
-- This is a worked practice solution, not evidence of production experience.

CREATE TEMP TABLE activation_case (
    week_order INTEGER NOT NULL,
    week TEXT NOT NULL,
    channel TEXT NOT NULL,
    eligible_users INTEGER NOT NULL CHECK (eligible_users > 0),
    activated_users INTEGER NOT NULL
        CHECK (activated_users >= 0 AND activated_users <= eligible_users),
    PRIMARY KEY (week_order, channel)
);

INSERT INTO activation_case VALUES
    (1, 'Last week', 'Organic', 1000, 200),
    (1, 'Last week', 'Paid',    1000, 100),
    (2, 'This week', 'Organic', 500, 110),
    (2, 'This week', 'Paid',   1500, 180);

-- 1. Channel rates and shares. Use decimal arithmetic to avoid integer division.
WITH weekly_totals AS (
    SELECT week_order, SUM(eligible_users) AS total_users
    FROM activation_case
    GROUP BY week_order
)
SELECT c.week, c.channel, c.eligible_users, c.activated_users,
       ROUND(100.0 * c.activated_users / c.eligible_users, 2)
           AS activation_rate_pct,
       ROUND(100.0 * c.eligible_users / t.total_users, 2)
           AS traffic_share_pct
FROM activation_case c
JOIN weekly_totals t ON c.week_order = t.week_order
ORDER BY c.week_order, c.channel;

-- 2. Aggregate rates must use summed counts, not the unweighted mean of rates.
SELECT week,
       SUM(eligible_users) AS eligible_users,
       SUM(activated_users) AS activated_users,
       ROUND(100.0 * SUM(activated_users) / SUM(eligible_users), 2)
           AS activation_rate_pct
FROM activation_case
GROUP BY week_order, week
ORDER BY week_order;

-- 3. Separate changes in rates from changes in weights.
-- This decomposition first changes rates at last week's mix, then changes mix
-- at this week's rates. Its "effects" are accounting components, not causal effects.
WITH weekly_totals AS (
    SELECT week_order, SUM(eligible_users) AS total_users
    FROM activation_case
    GROUP BY week_order
),
channel_metrics AS (
    SELECT c.week_order, c.channel,
           1.0 * c.activated_users / c.eligible_users AS rate,
           1.0 * c.eligible_users / t.total_users AS weight
    FROM activation_case c
    JOIN weekly_totals t ON c.week_order = t.week_order
),
paired AS (
    SELECT a.channel, a.rate AS old_rate, b.rate AS new_rate,
           a.weight AS old_weight, b.weight AS new_weight
    FROM channel_metrics a
    JOIN channel_metrics b ON a.channel = b.channel
    WHERE a.week_order = 1 AND b.week_order = 2
)
SELECT
    ROUND(100.0 * SUM(old_weight * old_rate), 2) AS last_week_pct,
    ROUND(100.0 * SUM(new_weight * new_rate), 2) AS this_week_pct,
    ROUND(100.0 * SUM(old_weight * new_rate), 2) AS fixed_old_mix_pct,
    ROUND(100.0 * SUM(new_weight * old_rate), 2) AS old_rates_new_mix_pct,
    ROUND(100.0 * SUM(old_weight * (new_rate - old_rate)), 2)
        AS within_channel_component_pp,
    ROUND(100.0 * SUM((new_weight - old_weight) * new_rate), 2)
        AS mix_component_pp,
    ROUND(100.0 * SUM(new_weight * new_rate - old_weight * old_rate), 2)
        AS net_change_pp
FROM paired;
