CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE IF NOT EXISTS public.users
(
    uuid       uuid PRIMARY KEY     DEFAULT uuid_generate_v4(),
    email      TEXT UNIQUE NOT NULL,
    password   TEXT        NOT NULL,
    login      TEXT        NOT NULL,
    full_name  TEXT        NOT NULL,
    phone      TEXT        NOT NULL,
    photo      TEXT        NOT NULL,
    location   point       NOT NULL,
    role       TEXT        NOT NULL,
    created_at timestamp   NOT NULL DEFAULT current_timestamp,
    updated_at timestamp   NOT NULL DEFAULT current_timestamp
);

CREATE TABLE IF NOT EXISTS public.events
(
    uuid           uuid PRIMARY KEY     DEFAULT uuid_generate_v4(),
    header         TEXT        NOT NULL,
    second_header  TEXT,
    location       point       NOT NULL,
    address        TEXT        NOT NULL,
    phone          TEXT UNIQUE NOT NULL,
    other_contacts TEXT,
    author_uuid    uuid        NOT NULL,
    url            TEXT,
    photo          TEXT,
    start_date     timestamp   not null,
    end_date       timestamp   not null,
    created_at     timestamp   not null default current_timestamp,
    updated_at     timestamp   not null default current_timestamp,
    FOREIGN KEY (author_uuid) REFERENCES public.users (uuid) ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS public.tags
(
    uuid uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    tag  TEXT UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS public.users_tags
(
    uuid      uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_uuid uuid NOT NULL,
    tag_uuid  uuid NOT NULL,
    FOREIGN KEY (user_uuid) REFERENCES public.users (uuid) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (tag_uuid) REFERENCES public.tags (uuid) ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS public.events_tags
(
    uuid       uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    event_uuid uuid NOT NULL,
    tag_uuid   uuid NOT NULL,
    FOREIGN KEY (event_uuid) REFERENCES public.events (uuid) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (tag_uuid) REFERENCES public.tags (uuid) ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS public.users_events
(
    uuid       uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_uuid  uuid NOT NULL,
    event_uuid uuid NOT NULL,
    FOREIGN KEY (user_uuid) REFERENCES public.users (uuid) ON UPDATE CASCADE ON DELETE RESTRICT,
    FOREIGN KEY (event_uuid) REFERENCES public.events (uuid) ON UPDATE CASCADE ON DELETE CASCADE
);
