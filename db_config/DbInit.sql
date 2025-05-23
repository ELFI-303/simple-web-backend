use db;

CREATE TABLE incomming_events(
    event_id int NOT NULL AUTO_INCREMENT,
    title varchar(200) NOT NULL,
    event_description varchar(500) NOT NULL,
    event_date datetime NOT NULL,
    place varchar(200) NOT NULL,
    img_url varchar(400) NOT NULL,
    link varchar(300) NOT NULL,
    PRIMARY KEY (event_id)
);

CREATE TABLE current_projects(
    project_id int NOT NULL AUTO_INCREMENT,
    title varchar(200) NOT NULL,
    project_description varchar(500) NOT NULL,
    project_date datetime NOT NULL,
    place varchar(200),
    img_url varchar(400),
    link varchar(300),
    equipe varchar(500) NOT NULL,
    PRIMARY KEY (project_id)
);

CREATE TABLE last_kahouts(
    kahout_id int NOT NULL AUTO_INCREMENT,
    title varchar(200) NOT NULL,
    kahout_date datetime NOT NULL,
    img_url varchar(400),
    PRIMARY KEY (kahout_id)
);

CREATE TABLE kahout_interview(
    question_id int NOT NULL AUTO_INCREMENT,
    kahout_id int NOT NULL,
    question varchar(500) NOT NULL,
    reponse varchar(500) NOT NULL,
    taux float NOT NULL,
    PRIMARY KEY (question_id)
);

CREATE TABLE question_received(
    question_received_id int NOT NULL AUTO_INCREMENT,
    question_date datetime NOT NULL,
    nom varchar(500) NOT NULL,
    email varchar(500) NOT NULL,
    message_envoye varchar(500) NOT NULL,
    PRIMARY KEY (question_received_id)
);

INSERT INTO `incomming_events`( title, event_description, event_date, place, img_url, link) VALUES("Sustainable Energy Workshop", "A hands-on workshop to explore renewable energy solutions, including solar panels and wind turbines, aimed at promoting sustainable energy practices.", "2024-12-05", "La Machinerie, Amiens, France", "https://images.unsplash.com/photo-1508341599442-4e4d6b3a8e6c", "https://example.com/event1"), ("Urban Gardening for Beginners", "Learn the basics of urban gardening and how to transform small spaces into productive green areas. Perfect for apartment dwellers!", "2024-12-10", "Maison de la Nature et de l’Environnement, Lille, France", "https://images.unsplash.com/photo-1516455207990-7a41ce80f7ee", "https://example.com/event2"), ("Plastic-Free Living Seminar", "Join environmental experts to discuss practical steps to reduce plastic usage and live a more sustainable lifestyle.", "2024-12-18", "Le Forum, Rouen, France", "https://images.unsplash.com/photo-1578589315946-1db078e0d720", "https://example.com/event3"), ("Circular Economy Hackathon", "A weekend hackathon where participants brainstorm and develop solutions for implementing a circular economy in local industries.", "2025-01-20", "Campus Cité Scientifique, Villeneuve-d'Ascq, France", "https://images.unsplash.com/photo-1596514314967-5c76e00c31f3", "https://example.com/event4"), ("Climate Action Film Festival", "Enjoy a series of inspiring documentaries and short films on climate change, followed by panel discussions with environmentalists and filmmakers.", "2025-02-15", "Théâtre Sébastopol, Lille, France", "https://images.unsplash.com/photo-1502209524168-aca5fa22c3f8", "https://example.com/event5"), ("Green Mobility Expo", "Explore the future of eco-friendly transportation with electric vehicles, e-bikes, and other sustainable mobility innovations.", "2025-02-28", "Parc Expo, Rouen, France", "https://images.unsplash.com/photo-1540574163026-643ea20ade25", "https://example.com/event6"), ("Eco-Building Conference", "A conference showcasing sustainable architecture and building practices, featuring leading industry experts.", "2025-03-12", "Palais des Congrès, Le Havre, France", "https://images.unsplash.com/photo-1542831371-29b0f74f9713", "https://example.com/event7"), ("Composting Made Easy", "Learn the fundamentals of composting, including how to set up and maintain a compost system at home.", "2025-03-20", "Les Jardins Suspendus, Le Havre, France", "https://images.unsplash.com/photo-1518976024611-38a9bf1e3be9", "https://example.com/event8"), ("Zero-Waste Challenge Kickoff", "A three-week program starting with a kickoff event to help participants adopt zero-waste habits and reduce their environmental footprint.", "2025-04-01", "Espace Citoyen, Dunkerque, France", "https://images.unsplash.com/photo-1556910103-df7fa8c2b4f8", "https://example.com/event9"), ("Sustainable Fashion Show", "A showcase of eco-friendly clothing lines and workshops on ethical fashion practices.", "2025-04-15", "La Condition Publique, Roubaix, France", "https://images.unsplash.com/photo-1567640892132-3aa51d6f51c5", "https://example.com/event10");
