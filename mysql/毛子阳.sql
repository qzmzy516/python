-- 要求使用SQL统计出每个用户的累积访问次数
with tmp as
         (select userId,
                 visitDate,
                 visitCount,
                 sum(visitCount) over (partition by userId order by userid
                     rows between unbounded preceding and current row ) as total_sum,
                 sum(visitCount) over (partition by userid,month(visitDate)
                     rows between unbounded preceding and current row ) as month_sum
          from test.test1),

     sum_type as (
         select userId,
                visitDate,
                visitCount,
                total_sum,
                month_sum,
                max(month_sum) over (partition by userid,month(visitDate)) as max_count
         from tmp
     )

select userId                          as 用户id,
       date_format(visitDate, '%Y-%m') as 月份,
       month_sum                       as 小计,
       total_sum                       as 累积
from sum_type
where max_count = month_sum;
-- 解题思路：
# 1.分析结果集可以得知，需要的指标有两个，一个是每个人每月的累计，还有一个是每个人总累计


