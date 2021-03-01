CREATE TABLE ride_sharing (rider_id INTEGER PRIMARY KEY AUTOINCREMENT, number_of_rides INTEGER, billing INTEGER, driver_id INTEGER);

INSERT INTO ride_sharing(number_of_rides, billing,driver_id ) VALUES (5, 100, 2);

INSERT INTO ride_sharing(number_of_rides, billing,driver_id ) VALUES (1, 20, 2);
INSERT INTO ride_sharing(number_of_rides, billing,driver_id ) VALUES (0, 0, Null);
INSERT INTO ride_sharing(number_of_rides, billing,driver_id ) VALUES (10, 250, 1);
INSERT INTO ride_sharing(number_of_rides, billing,driver_id ) VALUES (7, 140, 1);
INSERT INTO ride_sharing(number_of_rides, billing,driver_id ) VALUES (100, 2250, 3);

SELECT " Write a query to find out how many trips have been made by each driver this month, and how much they will be paid"; 
SELECT '----------------------------------------------------';

SELECT driver_id, SUM(number_of_rides), SUM(billing) as driver_payment FROM ride_sharing group by driver_id; 


SELECT "Write a query to find all the riders who haven't taken any trips this month. (So we can send them an irritating marketing email!)"; 
SELECT '----------------------------------------------------';

SELECT rider_id,
CASE
    WHEN number_of_rides > 10 THEN 'You are on a roll'
    WHEN number_of_rides > 5 THEN 'Keep going'
    ELSE "You haven't taken any trips yet"
END AS marketing_email
FROM ride_sharing;
