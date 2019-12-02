
# Checking 'updated_at' and 'count_visits' fields
>>> obj = Post.objects.get(title='NewPost')
>>> obj.count_visits
16
>>> obj.updated_at
datetime.datetime(2019, 12, 1, 18, 4, 39, 710819, tzinfo=<UTC>)


# Updating 'count_visits' and incrementing it by 1 doesn't change 'updated_at' field
>>> Post.objects.filter(title='NewPost').update(count_visits = F('count_visits') + 1)
1
>>> obj = Post.objects.get(title='NewPost')
>>> obj.count_visits  # only this field changed and incremented by one 
17
>>> obj.updated_at
datetime.datetime(2019, 12, 1, 18, 4, 39, 710819, tzinfo=<UTC>) # After using F(); 'updated_at' fields remains the same


#  Checking 'updated_at' and 'count_visits' fields
>>> obj = Post.objects.get(title='NewPost')
>>> obj.updated_at
datetime.datetime(2019, 12, 1, 18, 42, 46, 754476, tzinfo=<UTC>)
>>> obj.count_visits
20

# Updating 'count_visits' and incrementing it by 1 causes 'updated_at' field to change either
>>> obj = Post.objects.get(title='NewPost')
>>> obj.count_visits += 1
>>> obj.save()
>>> obj.count_visits
21
>>> obj.updated_at
datetime.datetime(2019, 12, 1, 18, 46, 27, 688457, tzinfo=<UTC>)