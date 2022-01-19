--
-- PostgreSQL database dump
--

-- Dumped from database version 14.1
-- Dumped by pg_dump version 14.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: actors; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.actors (
    id integer NOT NULL,
    fullname character varying(255) NOT NULL,
    dob date NOT NULL,
    best_films text
);


ALTER TABLE public.actors OWNER TO postgres;

--
-- Name: actors_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.actors_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.actors_id_seq OWNER TO postgres;

--
-- Name: actors_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.actors_id_seq OWNED BY public.actors.id;


--
-- Name: film_directors; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.film_directors (
    id integer NOT NULL,
    fullname character varying(255) NOT NULL,
    dob date NOT NULL,
    best_films text NOT NULL
);


ALTER TABLE public.film_directors OWNER TO postgres;

--
-- Name: film_directors_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.film_directors_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.film_directors_id_seq OWNER TO postgres;

--
-- Name: film_directors_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.film_directors_id_seq OWNED BY public.film_directors.id;


--
-- Name: films; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.films (
    id integer NOT NULL,
    title character varying(255) NOT NULL,
    release date,
    casts text
);


ALTER TABLE public.films OWNER TO postgres;

--
-- Name: films_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.films_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.films_id_seq OWNER TO postgres;

--
-- Name: films_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.films_id_seq OWNED BY public.films.id;


--
-- Name: actors id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.actors ALTER COLUMN id SET DEFAULT nextval('public.actors_id_seq'::regclass);


--
-- Name: film_directors id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.film_directors ALTER COLUMN id SET DEFAULT nextval('public.film_directors_id_seq'::regclass);


--
-- Name: films id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.films ALTER COLUMN id SET DEFAULT nextval('public.films_id_seq'::regclass);


--
-- Data for Name: actors; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.actors (id, fullname, dob, best_films) FROM stdin;
1	Matthew McConaughey	1969-11-04	The Gentlemen
2	Kate Winslet	1975-10-05	The Reader
3	Al Pacino	1940-04-25	Scent of a Woman
\.


--
-- Data for Name: film_directors; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.film_directors (id, fullname, dob, best_films) FROM stdin;
1	Guy Ritchie	1968-09-10	The Gentlemen
2	Quentin Tarantino	1963-04-27	Pulp Fiction
3	David Fincher	1962-08-28	Fight Club
\.


--
-- Data for Name: films; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.films (id, title, release, casts) FROM stdin;
1	Fight Club	1999-11-11	\N
2	Pulp Fiction	1994-10-14	\N
3	Scent of a Woman	1992-12-23	\N
\.


--
-- Name: actors_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.actors_id_seq', 3, true);


--
-- Name: film_directors_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.film_directors_id_seq', 3, true);


--
-- Name: films_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.films_id_seq', 3, true);


--
-- Name: actors actors_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.actors
    ADD CONSTRAINT actors_pkey PRIMARY KEY (id);


--
-- Name: film_directors film_directors_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.film_directors
    ADD CONSTRAINT film_directors_pkey PRIMARY KEY (id);


--
-- Name: films films_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.films
    ADD CONSTRAINT films_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

