WITH DuplicateEmails AS (
    SELECT email, MIN(id) as min_id
    FROM Person
    GROUP BY email
    HAVING COUNT(*) > 1
)
DELETE FROM Person
WHERE id NOT IN (SELECT min_id FROM DuplicateEmails)
  AND email IN (SELECT email FROM DuplicateEmails);
