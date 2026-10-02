# Write your MySQL query statement below

select p.firstname,p.lastname,a.city,a.state
from Person p
LEFT JOIN Address a ON p.personID=a.PersonID