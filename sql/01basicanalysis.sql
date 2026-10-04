SELECT Project_Type, COUNT(*) AS Number_of_Projects
FROM construction_projects
GROUP BY Project_Type
ORDER BY Number_of_Projects DESC;