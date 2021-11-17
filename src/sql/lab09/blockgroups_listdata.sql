SELECT
    year,
    geo_id,
    pop_density
FROM lab09.model_blockgroups
WHERE year = (SELECT MAX(year) from lab09.model_blockgroups)
ORDER BY pop_density DESC
LIMIT 5
