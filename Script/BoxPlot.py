plt.figure(figsize=(12,5))
columns=['operator_platform_age_years',
       'operator_platform_age_months', 'operator_active_years',
       'operator_active_months', 'operator_portfolio_size', 'geo_lat',
       'geo_lon', 'max_seats', 'utility_rooms', 'zones', 'workstations',
       'min_term_days', 'max_term_days', 'min_term_floor', 'min_term_ceiling',
       'max_term_floor', 'max_term_ceiling', 'min_term_avg', 'max_term_avg',
       'open_slots_a', 'open_slots_b', 'open_slots_c', 'open_slots_d',
       'review_count', 'review_count_12m', 'review_count_30d', 'open_slots_e',
       'review_count_prev_yr', 'booked_load', 'score_overall',
       'score_accuracy', 'score_condition', 'score_onboarding',
       'score_support', 'score_access', 'score_value', 'operator_metro_units',
       'operator_metro_whole', 'operator_metro_private',
       'operator_metro_shared', 'reviews_per_month', 'price_tier']

sns.boxplot(
    data=train[columns],
    orient='h',
    color="skyblue",
    flierprops={'markerfacecolor' : 'red', 'marker' : 'o'}
)

plt.grid(axis='x',linestyle='--',alpha=0.5)
plt.tight_layout()
plt.show
