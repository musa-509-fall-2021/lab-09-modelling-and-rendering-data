SELECT
    year,
    SUM(male_pop) AS total_male_pop,
    SUM(female_pop) AS total_female_pop,
    SUM(white_pop) AS total_white_pop,
    SUM(black_pop) AS total_black_pop,
    SUM(asian_pop) AS total_asian_pop,
    SUM(hispanic_pop) AS total_hispanic_pop,
    SUM(amerindian_pop) AS total_amerindian_pop,
    SUM(other_race_pop) AS total_other_race_pop,
    SUM(two_or_more_races_pop) AS total_two_or_more_races_pop
FROM lab09.model_blockgroups
GROUP BY year
