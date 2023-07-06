
metric_ids = ["1_DAILY", "2_DAILY", "3_DAILY"]

def check_data(metric_ids):
    # Remove the "_DAILY" suffix from each value using list comprehension
    metric_ids = [metric_id.replace("_DAILY", "") for metric_id in metric_ids]

    # Join the modified values with commas and format them in the WHERE clause
    where_clause = "WHERE metric_id IN ({})".format(", ".join(metric_ids))
    print(where_clause)

check_data(metric_ids)    

