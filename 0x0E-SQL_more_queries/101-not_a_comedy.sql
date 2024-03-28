-- To list shows without the genre comedy in the database
-- Results are ordered in ascending by show title
SELECT DISTINCT `title`
  FROM `tv_shows` AS t
       LEFT JOIN `tv_show_genres` AS ts
       ON ts.`show_id` = t.`id`

       LEFT JOIN `tv_genres` AS g
       ON g.`id` = ts.`genre_id`
       WHERE t.`title` NOT IN
	     (SELECT `title`
		FROM `tv_shows` AS t
		     INNER JOIN `tv_show_genres` AS ts
		     ON s.`show_id` = t.`id`

		     INNER JOIN `tv_genres` AS g
		     ON g.`id` = ts.`genre_id`
		     WHERE g.`name` = "Comedy")
ORDER BY `title`;
