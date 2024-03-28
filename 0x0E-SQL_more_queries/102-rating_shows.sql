-- To list all shows from hbtn_0d_tvshows_rate by rating
-- results are sorted in descending order by rating
SELECT `title`, SUM(`rate`) AS `rating`
  FROM `tv_shows` AS t
       INNER JOIN `tv_show_ratings` AS tr
       ON t.`id` = tr.`show_id`
GROUP BY `title`
ORDER BY `rating` DESC;
