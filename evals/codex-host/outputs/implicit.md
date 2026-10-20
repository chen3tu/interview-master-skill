**The overall rate fell because traffic shifted toward paid acquisition, the lower-activation channel.** Both channels improved, but the mix shift outweighed those gains—an example of Simpson’s paradox.

| Metric | Last week | This week |
|---|---:|---:|
| Organic activation | 200/1,000 = **20%** | 110/500 = **22%** |
| Paid activation | 100/1,000 = **10%** | 180/1,500 = **12%** |
| Paid share of users | **50%** | **75%** |
| Overall activation | 300/2,000 = **15%** | 290/2,000 = **14.5%** |

A complete answer to practice aloud:

> “Both observations are correct because the overall activation rate is a weighted average.
>
> “Organic activation increased from 20% to 22%, and paid activation increased from 10% to 12%. However, paid traffic grew from 50% to 75% of all users. Since paid still has the lower activation rate, its increased weight pulled down the overall result.
>
> “Holding last week’s 50/50 mix constant, this week’s rates would produce 17% activation: half of 22% plus half of 12%. That represents a two-percentage-point improvement. Moving to this week’s actual mix reduces the result by 2.5 percentage points, giving 14.5%. So the net change is a decline of half a percentage point.
>
> “Before acting, I would check that eligibility, activation definitions, channel attribution, and observation windows are consistent across both weeks. I would then investigate why organic volume fell and paid volume increased, and examine acquisition costs, retention, and downstream value.
>
> “I would report actual activation alongside channel rates and a fixed-mix comparison. This explains the aggregate decline, but it does not prove that a product change caused the channel improvements.”

Your complete materials are ready:

- [English practice packet](interview_practice.md): spoken answer, decision memo, follow-up answers, experiment-experience wording, and practice exercises.
- [Runnable SQL work sample](work_sample.sql): supplied inputs, channel metrics, overall rates, and decomposition. **Executed successfully in SQLite; all results matched.**

For experience questions, keep this boundary clear: **“I have basic SQL skills and have worked on a course retention dashboard. I have not run a production experiment.”** Present this analysis as a practice work sample.

Used the project’s interview-master skill entirely offline. No other personal files were read, and no skills were modified. Files are in a temporary folder. Your next practice step is to explain the result from memory, then answer: “Would you reduce paid acquisition, and what additional evidence would you need?”