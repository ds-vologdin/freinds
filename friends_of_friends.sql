CREATE TABLE "users" (
  "id" serial NOT NULL PRIMARY KEY,
  "username" varchar(50) NOT NULL UNIQUE,
  "name" varchar(200) NOT NULL,
  "birthday" date NULL
);

CREATE TABLE "friends" (
  "id" serial NOT NULL PRIMARY KEY,
  "from_user_id" integer NOT NULL,
  "to_user_id" integer NOT NULL,
  FOREIGN KEY ("from_user_id") REFERENCES "users" ("id") ON DELETE CASCADE,
  FOREIGN KEY ("to_user_id") REFERENCES "users" ("id") ON DELETE CASCADE
);

CREATE TABLE "request_friend" (
  "id" serial NOT NULL PRIMARY KEY,
  "message" text NOT NULL,
  "datetime_request" timestamp with time zone NOT NULL,
  "datetime_accept" timestamp with time zone NULL,
  "status" varchar(6) NOT NULL,
  "from_user_id" integer NOT NULL,
  "to_user_id" integer NOT NULL,
  FOREIGN KEY ("from_user_id") REFERENCES "users" ("id") ON DELETE CASCADE,
  FOREIGN KEY ("to_user_id") REFERENCES "users" ("id") ON DELETE CASCADE
)

CREATE INDEX friends_from_user_id_indx ON friends (from_user_id);
CREATE INDEX friends_to_user_id_indx ON friends (to_user_id);

WITH RECURSIVE r AS (
    SELECT from_user_id, to_user_id
	FROM friends
	WHERE from_user_id=3
    UNION
    SELECT friends.from_user_id, friends.to_user_id
	FROM friends JOIN r ON r.from_user_id = friends.to_user_id
)
SELECT from_user_id, to_user_id FROM r ORDER BY from_user_id;
