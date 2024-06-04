HBnB Evolution: Part 1 (Model + API)

Description:

Welcome to the firts leg of our exciting journey-creating our very own web
application, HBnB Evolution modeled  after AirBnb, using Python and Flask!.

What’s Cooking in Part 1?

Sketching with UML:

-Draw the backbone of our application using UML (Unified Modeling Language).
-Create the architectural blueprint for classes and components interaction.
-Testing Our Logic:

-Set up tests for the API and business logic to ensure smooth functioning.
-Building the API:

-Implement the API using Flask.
-Integrate it with business logic and file-based persistence.
-File-Based Data Storage:

-Utilize a file-based system for storing data (e.g., text, JSON, XML).
-Design it for easy migration to a database in the future.
-Packaging with Docker:

-Wrap the application in a Docker image for easy deployment.
-The Three Layers of Our API Cake:
-Services Layer:

-Handles API requests and responses.
-Business Logic Layer:

-Processes data and makes decisions.
-Persistence Layer:

-Currently file-based storage; will transition to a database later.
-The Data Model: Key Entities
-Places: Heart of the app, with attributes like name, description, address, etc.
-Users: Owners (hosts) or reviewers (commenters) of places.
-Reviews: User feedback and ratings for places.
-Amenities: Features of places.
-Country and City: Essential for categorizing and searching places.
-Business Logic: Rules to Live By
-Unique Users
-One Host per Place
-Flexible Hosting
-Open Reviewing
-Amenity Options
-City-Country Structure
-Standard Attributes for Every Entity:
-Unique ID (UUID4)
-Creation Date (created_at)
-Update Date (updated_at)
-Why These Attributes Matter?
-Uniqueness: Ensures each entity is distinct.
-Traceability: Tracks the lifecycle of each entity for debugging and auditing.

As you design and implement these features, remember to keep scalability and maintainability in mind for future enhancements. Happy coding!
