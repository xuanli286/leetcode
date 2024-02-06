select sub1.user_id, round(coalesce(cfm/tol, 0), 2) as confirmation_rate from 
(select s.user_id, count(*) as tol from signups s
left join confirmations c
on s.user_id=c.user_id
group by s.user_id) sub1
left join
(select *, count(*) as cfm from confirmations
where action='confirmed'
group by user_id) sub2
on sub1.user_id=sub2.user_id