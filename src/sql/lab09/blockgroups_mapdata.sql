-- The following query uses the NTILE function to assign each blockgroup into
-- one of five bins according to its pop_density during the latest available
-- year. To see more about NTILE:
--
-- https://cloud.google.com/bigquery/docs/reference/standard-sql/numbering_functions#ntile

SELECT
    geo_id,
    pop_density,
    NTILE(5) OVER (ORDER BY pop_density) as binned_pop_density,
    blockgroup_geom
FROM lab09.model_blockgroups
WHERE year = (SELECT MAX(year) from lab09.model_blockgroups)
