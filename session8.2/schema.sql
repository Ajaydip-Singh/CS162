CREATE TABLE runners(runned_id INTEGER PRIMARY KEY, 
		     	first_name VARCHAR(60), 
			last_name VARCHAR(60), 
			email TEXT),
			age INTEGER, 
			gender INTEGER)

CREATE TABLE races(race_id INTEGER PRIMARY KEY, 
			name VARCHAR(70),
			date DATETIME)

CREATE TABLE runner_race(runner_id INTEGER PRIMARY KEY,
		  	race_id INTEGER PRIMARY KEY)

CREATE TABLE race_challenge(race_id, 
			challenge_id)


CREATE TABLE challenges(challenge_id INTEGER PRIMARY KEY, 
			name VARCHAR(60))


