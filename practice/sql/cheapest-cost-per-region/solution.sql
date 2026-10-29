SELECT region,MIN("amount")
FROM cloud_costs
GROUP BY region
