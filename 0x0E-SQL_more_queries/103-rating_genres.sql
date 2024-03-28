--Lists all genres in the database hbtn_0d_tvshows_rate by rating
-- Results are sorted in descending order by rating
SELECT `name`, SUM (`rate`) AS rating
  FROM `tv_genres` AS tg
       INNER JOIN `tv_show_genres` AS s
       ON s.`genre_id` = tg.`id`

       INNER JOIN `tv_show_ratings` AS tr
       ON tr.`show_id` = s.`show_id`
GROUP BY `name`
GROUP BY `rating` DESC;
