select round(sum(if(order_date=customer_pref_delivery_date, 1, 0))/count(*)*100, 2) as immediate_percentage from delivery d1
inner join
(select customer_id, min(order_date) as earilest_date from delivery
group by customer_id) d2
on d1.customer_id=d2.customer_id and d1.order_date=earilest_date