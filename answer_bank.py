from typing import Dict, List

AnswerSet = Dict[str, str]
AnswerBank = Dict[str, Dict[str, List[AnswerSet]]]

answer_bank: AnswerBank = {

    "Programming & Object-Oriented Concepts": {

        "Easy": [
            {
                "correct": "A variable is a named memory location that stores a value which can change during execution. It allows programs to reference and manipulate data using meaningful names instead of raw values, making code reusable and readable.",
                "partial": "A variable stores data in a program and can hold values like numbers or text.",
                "incorrect": "A variable is a fixed constant that cannot be changed once assigned. It stores values permanently in the CPU cache."
            },
            {
                "correct": "A list is mutable, defined with square brackets [], allowing elements to be added, removed, or changed. A tuple is immutable, defined with parentheses (), and cannot be modified after creation. Tuples use less memory and are faster, making them suitable for fixed data.",
                "partial": "A list can be changed after creation but a tuple cannot. Lists use [] and tuples use ().",
                "incorrect": "Lists and tuples are identical. Tuples use curly braces {} while lists use square brackets. Both are mutable."
            },
            {
                "correct": "A function is a named, reusable block of code that performs a specific task, accepts parameters, and can return values. Benefits include code reuse, improved readability, reduced duplication, easier debugging, and modular design.",
                "partial": "A function is a block of code that does a specific task. It helps reuse code and keeps programs organised.",
                "incorrect": "A function is a variable that stores multiple values. It runs code in parallel on multiple processors to improve speed."
            },
            {
                "correct": "A dictionary stores data as key-value pairs using curly braces {}. Keys must be unique and immutable while values can be any type. It provides O(1) average-time lookup using a hash table internally, useful when accessing data by a meaningful identifier.",
                "partial": "A dictionary stores data as key-value pairs and values are accessed using their keys. It uses curly braces.",
                "incorrect": "A dictionary translates text between languages. It sorts all words alphabetically for fast searching like a real dictionary."
            },
            {
                "correct": "Object-Oriented Programming organises software around objects, which are instances of classes bundling data and behaviour together. The four core principles are Encapsulation, Abstraction, Inheritance, and Polymorphism, promoting code reuse, modularity, and maintainability.",
                "partial": "OOP uses classes and objects to organise code. It helps reuse code and models real-world entities.",
                "incorrect": "OOP is a database design technique where data is stored in tables called objects. It was introduced in Python and is unavailable in other languages."
            },
        ],

        "Medium": [
            {
                "correct": "A class is a blueprint that defines attributes and methods. An object is a specific instance created from a class with its own attribute values. For example, Car is a class with colour and speed attributes, while my_car = Car() is a concrete object. Multiple objects can be created from one class.",
                "partial": "A class is a template and an object is an instance of that class containing actual values.",
                "incorrect": "A class and an object are the same thing. You can only create one object per class."
            },
            {
                "correct": "Inheritance allows a child class to acquire attributes and methods of a parent class, establishing an is-a relationship and promoting code reuse. For example, Dog inherits from Animal and gains its speak() method while adding its own fetch() method. Python supports single, multiple, and multilevel inheritance.",
                "partial": "Inheritance lets a child class use the methods and attributes of a parent class. A Dog class can inherit from an Animal class.",
                "incorrect": "Inheritance means copying all code from one class into another manually to reduce the number of files in a project."
            },
            {
                "correct": "Encapsulation bundles data and methods within a single class and restricts direct external access using private attributes (prefixed with _ or __). Public getter and setter methods provide controlled access. It protects internal state, reduces complexity, and makes code easier to maintain.",
                "partial": "Encapsulation hides internal class details from outside code using private variables and methods.",
                "incorrect": "Encapsulation converts a class into a capsule file for deployment. It compresses code so the program runs faster."
            },
            {
                "correct": "Exception handling manages runtime errors without crashing the program using try-except-else-finally blocks. Code that may fail goes in try, except catches specific exceptions, else runs when no exception occurs, and finally always runs for cleanup. Custom exceptions are created by inheriting from the Exception class.",
                "partial": "Exception handling uses try and except blocks. The try block contains risky code and except handles the error.",
                "incorrect": "Exception handling uses catch and throw keywords in Python. It prevents compilation when there is a syntax error."
            },
            {
                "correct": "A Python module is a file containing functions, classes, and variables that can be imported into other programs using the import statement. Modules organise code into logical reusable units, prevent duplication, and keep programs manageable. Python includes a standard library of built-in modules like os, sys, and math.",
                "partial": "A Python module is a file with Python code that can be imported into other programs to reuse functions and classes.",
                "incorrect": "A Python module is a folder storing image and video files. It is imported using the load keyword and cannot contain functions."
            },
        ],

        "Hard": [
            {
                "correct": "Polymorphism allows objects of different classes to be treated through a common interface. In Python, method overriding and duck typing enable this. Different classes like Circle and Rectangle can each implement area(), and a function calling shape.area() works for all without knowing the specific type. This reduces duplication and improves extensibility.",
                "partial": "Polymorphism allows different classes to use the same method name with different behaviour, making code more flexible.",
                "incorrect": "Polymorphism means a single variable stores multiple values simultaneously. It allows the same program to run on multiple operating systems."
            },
            {
                "correct": "A decorator is a higher-order function that wraps another function to extend its behaviour without modifying the source code. It uses the @ syntax above the function definition, accepting a function as input and returning a wrapper. Use cases include logging, authentication, caching with functools.lru_cache, and access control in frameworks like Django.",
                "partial": "Decorators add extra functionality to a function using the @ symbol without changing the original code. Common examples are @staticmethod and @classmethod.",
                "incorrect": "Decorators change the visual appearance of terminal output. The @ symbol runs the function on a separate thread automatically."
            },
            {
                "correct": "A generator uses the yield keyword to produce values one at a time, pausing execution between each yield and resuming on the next request. It returns a generator object acting as an iterator. Benefits over lists include memory efficiency since values are generated on demand, lazy evaluation, and the ability to represent infinite sequences.",
                "partial": "Generators use yield and produce values one at a time instead of storing everything in memory, making them memory efficient.",
                "incorrect": "Generators are a type of list that sorts values automatically as they are added. They are slower than regular lists."
            },
            {
                "correct": "A shallow copy creates a new object but references the same nested objects as the original, so changes to nested mutable objects affect both. A deep copy recursively duplicates all nested objects creating complete independence. In Python, copy.copy() is shallow and copy.deepcopy() is deep. Use deep copy when full isolation between original and copy is required.",
                "partial": "Shallow copy copies only the top level while deep copy copies everything including nested objects. Deep copy is safer for nested data.",
                "incorrect": "Shallow copy compresses the object to save memory. Deep copy stores the object permanently on disk for later retrieval."
            },
            {
                "correct": "Python's threading module allows multiple threads within the same process sharing memory. The Global Interpreter Lock in CPython allows only one thread to execute bytecode at a time even on multi-core systems. This makes threading effective for I/O-bound tasks like file and network operations but ineffective for CPU-bound tasks. The multiprocessing module is used for CPU-bound parallelism since each process has its own GIL.",
                "partial": "Python supports multithreading using the threading module. The GIL prevents true parallel execution so threading works best for I/O-bound tasks.",
                "incorrect": "The GIL makes Python the fastest language for multithreaded programs by distributing threads across CPU cores automatically."
            },
        ],
    },

    "SQL & Database Systems": {

        "Easy": [
            {
                "correct": "A Database Management System is software that enables users to create, store, retrieve, update, and manage data in a structured way. It acts as an interface between users and the database, providing security, data integrity, concurrency control, backup and recovery, and query processing. Examples include MySQL, PostgreSQL, Oracle, and SQLite.",
                "partial": "A DBMS is software used to manage and store data. It allows users to create tables and run queries. Examples are MySQL and Oracle.",
                "incorrect": "A DBMS is a programming language used to write database applications. It is the same as Microsoft Excel and only handles spreadsheet data."
            },
            {
                "correct": "SQL is a standard language for communicating with relational databases. It handles DDL operations like CREATE and DROP for structure, DML operations like INSERT and DELETE for data, DQL with SELECT for retrieval, and DCL with GRANT and REVOKE for access control. SQL provides a simple and standardised way to interact with data across different database systems.",
                "partial": "SQL is used to interact with relational databases through commands like SELECT, INSERT, UPDATE, and DELETE.",
                "incorrect": "SQL stands for Software Query Logic and is used to build mobile apps. It is only compatible with Microsoft databases."
            },
            {
                "correct": "A primary key is a column or combination of columns that uniquely identifies each row in a table. It enforces uniqueness so no two rows share the same value and NOT NULL so it cannot be empty. Each table has only one primary key, which is also used as a reference target for foreign keys to establish relationships between tables.",
                "partial": "A primary key uniquely identifies each record in a table. It cannot be NULL or duplicate and links tables through foreign keys.",
                "incorrect": "A primary key is always the first column named ID and is automatically created by the database. It can contain duplicates in different rows."
            },
            {
                "correct": "A foreign key is a column in one table that references the primary key of another table, linking the two. It enforces referential integrity by preventing insertion of values that do not exist in the referenced column. For example, an Orders table may have a customer_id foreign key referencing the primary key of the Customers table.",
                "partial": "A foreign key links one table to another by referencing the primary key of the referenced table. It maintains referential integrity.",
                "incorrect": "A foreign key is imported from a foreign database standard. It is only used in NoSQL databases and not supported in SQL."
            },
            {
                "correct": "A database table is a structured collection of data organised in rows and columns. Each column represents an attribute with a specific data type and each row is a single record. Tables are the fundamental storage unit in relational databases. Related tables are linked through primary and foreign keys to form a complete relational database.",
                "partial": "A database table stores data in rows and columns where each row is a record and each column is a field.",
                "incorrect": "A database table is a visual dashboard displaying graphs and charts. It is used only for reporting and cannot store actual data."
            },
        ],

        "Medium": [
            {
                "correct": "Normalisation organises a relational database to reduce redundancy and improve data integrity by dividing large tables into smaller well-structured ones. First normal form requires atomic values with no repeating groups. Second normal form eliminates partial dependencies on the primary key. Third normal form eliminates transitive dependencies between non-key attributes. It prevents insert, update, and delete anomalies.",
                "partial": "Normalisation reduces data redundancy by dividing tables into smaller ones following rules called 1NF, 2NF, and 3NF.",
                "incorrect": "Normalisation converts all text to lowercase for consistency. It is performed only on NoSQL databases to improve query speed."
            },
            {
                "correct": "SQL joins combine rows from two or more tables based on a related column. INNER JOIN returns only matching rows from both tables. LEFT JOIN returns all rows from the left table with NULLs for unmatched right rows. RIGHT JOIN is the reverse. FULL OUTER JOIN returns all rows from both. CROSS JOIN returns the Cartesian product. Joins are essential for querying data across normalised tables.",
                "partial": "SQL joins combine data from multiple tables. INNER JOIN returns matching rows and LEFT JOIN returns all rows from the left table.",
                "incorrect": "SQL joins merge two database files into a single file permanently on disk. Only one type of join exists in SQL."
            },
            {
                "correct": "DELETE is a DML command removing specific rows using a WHERE clause and can be rolled back. It fires triggers and logs each deletion. TRUNCATE is a DDL command removing all rows at once, faster than DELETE, cannot use WHERE, resets identity counters, and generally cannot be rolled back. DROP permanently removes the entire table structure and data from the database.",
                "partial": "DELETE removes specific rows and can be rolled back. TRUNCATE removes all rows faster without WHERE. DROP removes the entire table permanently.",
                "incorrect": "All three do the same thing. DROP is the safest because it keeps the table structure. None can be rolled back."
            },
            {
                "correct": "An index is a data structure, typically a B-tree, that stores pointers to table rows based on column values to speed up retrieval. Without an index the database performs a full table scan at O(n). With an index lookup is O(log n). Indexes are created on columns used in WHERE, JOIN, and ORDER BY. The trade-off is slower INSERT, UPDATE, and DELETE operations because the index must be maintained.",
                "partial": "Indexing creates a data structure that speeds up SELECT queries by avoiding full table scans. It can slow down write operations.",
                "incorrect": "Indexing numbers all rows automatically. It speeds up all operations including INSERT and DELETE with no trade-offs."
            },
            {
                "correct": "ACID ensures reliable transactions. Atomicity means a transaction is all-or-nothing and rolls back completely on failure. Consistency brings the database from one valid state to another respecting all constraints. Isolation means concurrent transactions execute as if sequential with intermediate states invisible to others. Durability ensures committed data persists even after a crash using write-ahead logging.",
                "partial": "ACID stands for Atomicity, Consistency, Isolation, and Durability. Together they ensure database transactions are reliable and safe.",
                "incorrect": "ACID stands for Availability, Concurrency, Integrity, and Distribution. It applies only to NoSQL databases."
            },
        ],

        "Hard": [
            {
                "correct": "A transaction is a sequence of SQL operations treated as a single logical unit following ACID properties. Example: a bank transfer debits one account and credits another. If the credit fails the debit is rolled back. COMMIT saves changes permanently, ROLLBACK undoes them, and SAVEPOINT allows partial rollbacks within a transaction.",
                "partial": "A transaction groups SQL statements executed together. If one fails the entire transaction rolls back. A bank transfer is a common example.",
                "incorrect": "A database transaction is a scheduled nightly backup operation. It transfers data between two servers on a fixed schedule."
            },
            {
                "correct": "A deadlock occurs when two or more transactions each hold a lock the other needs, creating a circular wait. Prevention strategies include acquiring locks in a consistent order across transactions, using lock timeouts, keeping transactions short, and using optimistic concurrency control. Most databases auto-detect deadlocks using a wait-for graph and roll back the victim transaction.",
                "partial": "A deadlock happens when transactions wait for each other's locks. It is prevented by locking tables in a consistent order and keeping transactions short.",
                "incorrect": "A deadlock happens when the database runs out of memory and freezes. It is resolved by restarting the server and only occurs in NoSQL databases."
            },
            {
                "correct": "A clustered index determines the physical order of data rows in the table so the data itself is sorted by the index key. Only one clustered index is allowed per table. A non-clustered index is a separate structure storing index key values and pointers to the actual rows. Multiple non-clustered indexes are allowed. Clustered indexes suit range queries while non-clustered indexes support multiple lookup patterns.",
                "partial": "A clustered index physically sorts table data and only one is allowed. A non-clustered index is a separate structure with row pointers and multiple are allowed.",
                "incorrect": "A clustered index groups rows from different tables into one file. A non-clustered index is stored on a different server accessed over the network."
            },
            {
                "correct": "Sharding is horizontal scaling that partitions a large database into smaller independent pieces called shards, each on a separate server holding a subset of data based on a shard key. Strategies include range-based, hash-based, and directory-based sharding. It is used when a single server cannot handle the data volume or request load. Challenges include cross-shard queries and rebalancing.",
                "partial": "Sharding splits a large database into smaller parts on different servers. It is used when one server cannot handle the data volume alone.",
                "incorrect": "Sharding encrypts the database and splits the key for security. It is only used for backups and does not improve performance."
            },
            {
                "correct": "Concurrency control manages simultaneous database access to ensure consistency and isolation. Problems include dirty reads, non-repeatable reads, and phantom reads. Techniques include locking protocols with shared and exclusive locks, timestamp ordering, and Multiversion Concurrency Control where readers do not block writers, used in PostgreSQL. Isolation levels like READ COMMITTED and SERIALIZABLE define the degree of control applied.",
                "partial": "Concurrency control ensures multiple transactions do not cause inconsistency. It uses locking mechanisms and isolation levels.",
                "incorrect": "Concurrency control is a network protocol controlling server internet speed. It allows only one user to access the database at a time."
            },
        ],
    },

    "Machine Learning & AI": {

        "Easy": [
            {
                "correct": "Machine Learning is a subset of AI that enables systems to learn from data and improve performance without being explicitly programmed for each scenario. Algorithms identify patterns in data and use them to make predictions or decisions. It is categorised into supervised learning, unsupervised learning, and reinforcement learning.",
                "partial": "Machine Learning allows computers to learn from data and make predictions without being explicitly programmed. It is part of AI.",
                "incorrect": "Machine Learning is a hardware component that makes computers process data faster. It is a type of database that organises information automatically."
            },
            {
                "correct": "Artificial Intelligence is the broad field focused on building systems that perform tasks requiring human intelligence such as reasoning and language understanding. Machine Learning is a subset of AI that enables systems to learn from data without explicit programming. All Machine Learning is AI but not all AI is Machine Learning since AI also includes rule-based systems and expert systems.",
                "partial": "AI is a broad field that makes machines intelligent. Machine Learning is a subset of AI that allows machines to learn from data.",
                "incorrect": "AI and Machine Learning are the same and can be used interchangeably. Machine Learning is just the older term replaced by AI."
            },
            {
                "correct": "Supervised learning trains a model on labelled data where each input has a corresponding correct output. The model learns a mapping from inputs to outputs by minimising prediction error. It is divided into classification for predicting categories and regression for predicting continuous values. Examples include spam detection, house price prediction, and image classification.",
                "partial": "In supervised learning the model trains on labelled data where each input has a known output. It is used for classification and regression.",
                "incorrect": "Supervised learning is when a human supervises the training process manually at every step. The model cannot train without direct human supervision."
            },
            {
                "correct": "Unsupervised learning trains on unlabelled data and discovers hidden structure or patterns without predefined answers. Common tasks include clustering to group similar data points using algorithms like K-Means, dimensionality reduction using PCA, and anomaly detection. It is useful when labelled data is expensive or unavailable.",
                "partial": "In unsupervised learning the model finds patterns in data without labels. Clustering algorithms like K-Means are common examples.",
                "incorrect": "Unsupervised learning trains itself on the internet without any dataset. It is faster than supervised learning because it uses no data."
            },
            {
                "correct": "A dataset in Machine Learning is a structured collection of data used to train, validate, and test models. It consists of features as input variables and labels as target outputs in supervised learning. Datasets are split into training to fit the model, validation to tune hyperparameters, and test sets to evaluate final performance. Quality, size, and representativeness directly affect model performance.",
                "partial": "A dataset is a collection of data used to train a machine learning model. It is typically split into training and testing sets.",
                "incorrect": "A dataset is a single CSV file containing the source code of the model. It is only used after deployment, not during training."
            },
        ],

        "Medium": [
            {
                "correct": "Overfitting occurs when a model learns the training data too well including noise and outliers, resulting in excellent training performance but poor generalisation. Signs include very low training error with high validation error. Techniques to reduce it include regularisation, dropout in neural networks, cross-validation, early stopping, reducing model complexity, increasing training data, and data augmentation.",
                "partial": "Overfitting is when a model performs well on training data but poorly on new data. It is reduced using regularisation, dropout, or more training data.",
                "incorrect": "Overfitting means the model is too simple. It is fixed by adding more layers and increasing the learning rate."
            },
            {
                "correct": "Underfitting occurs when a model is too simple to capture underlying patterns, resulting in high error on both training and test sets. It happens when the model has too few parameters, insufficient training, or missing important features. Solutions include increasing model complexity, adding relevant features, reducing regularisation, and training for more epochs.",
                "partial": "Underfitting is when a model is too simple and fails to learn patterns, performing poorly on both training and test data.",
                "incorrect": "Underfitting is when the model trains with too much data and gets confused. It is the same as overfitting but happens during testing."
            },
            {
                "correct": "Feature engineering uses domain knowledge to create, transform, or select input variables from raw data to improve model performance. Techniques include creating new features from existing ones such as extracting year from a date, encoding categorical variables with one-hot or label encoding, scaling with normalisation or standardisation, handling missing values, and removing irrelevant features. It often has more impact than algorithm choice.",
                "partial": "Feature engineering creates and transforms input variables to improve model performance. Examples include encoding categorical data and scaling numerical features.",
                "incorrect": "Feature engineering means selecting the best algorithm for a problem. It is automated entirely by the model during training."
            },
            {
                "correct": "Classification is a supervised learning task where the goal is to predict which category an input belongs to from a predefined set of discrete classes. Binary classification has two classes such as spam or not spam. Multi-class classification has more than two. Common algorithms include Logistic Regression, Decision Trees, Random Forest, SVM, and Neural Networks. Metrics include accuracy, precision, recall, F1 score, and AUC-ROC.",
                "partial": "Classification is a supervised task where the model predicts the category of an input. Examples include spam detection and image recognition.",
                "incorrect": "Classification sorts the training dataset alphabetically before feeding it to the model. It has nothing to do with prediction."
            },
            {
                "correct": "Cross-validation provides a reliable estimate of model performance by training and testing on multiple different data splits. In k-fold cross-validation the data is divided into k equal folds, the model trains on k-1 folds and validates on the remaining fold, rotating k times, and the final score is the average. It avoids overfitting to a single split, makes full use of data, and enables fair model comparison.",
                "partial": "Cross-validation evaluates a model by training and testing on multiple splits. K-fold divides data into k parts and rotates the validation set for a reliable estimate.",
                "incorrect": "Cross-validation trains two models simultaneously and crosses their results. It only applies to deep learning and not traditional ML."
            },
        ],

        "Hard": [
            {
                "correct": "Gradient descent minimises a loss function by iteratively updating parameters in the direction of the negative gradient. The update rule is: parameter = parameter minus learning rate multiplied by gradient. Batch GD uses the entire dataset and is stable but slow. Stochastic GD uses one sample and is fast but noisy. Mini-batch GD uses small batches and balances speed and stability, being the standard in deep learning. Adaptive optimisers like Adam adjust learning rates per parameter automatically.",
                "partial": "Gradient descent minimises the loss by updating weights in the direction of the negative gradient. Mini-batch gradient descent is the most commonly used variant.",
                "incorrect": "Gradient descent randomly shuffles training data to improve accuracy. It increases the learning rate automatically until the model converges."
            },
            {
                "correct": "Bias is error from overly simplistic model assumptions causing underfitting. Variance is error from sensitivity to small changes in training data causing overfitting. Decreasing bias typically increases variance and vice versa. Total error equals bias squared plus variance plus irreducible error. The goal is optimal complexity minimising total error. Bagging like Random Forest reduces variance and boosting reduces bias.",
                "partial": "Bias is error from a model too simple and variance is error from a model too complex. The goal is to balance both for best generalisation.",
                "incorrect": "Bias means the dataset contains prejudiced data. Variance is the standard deviation of accuracy scores across epochs. High variance always means good performance."
            },
            {
                "correct": "Regularisation adds a penalty term to the loss function to discourage overly complex models and prevent overfitting. L1 or Lasso adds the sum of absolute weight values, driving some weights exactly to zero and performing implicit feature selection. L2 or Ridge adds the sum of squared weights, shrinking all weights toward zero without zeroing them. ElasticNet combines both. Regularisation improves generalisation by constraining model complexity.",
                "partial": "Regularisation adds a penalty to the loss function to prevent overfitting. L1 can zero weights for feature selection and L2 shrinks all weights without zeroing.",
                "incorrect": "Regularisation formats the dataset into a regular table structure. It increases training accuracy by removing negative values from the dataset."
            },
            {
                "correct": "Ensemble learning combines multiple models to produce a stronger predictor than any individual model. Bagging trains models on different random data subsets in parallel and aggregates predictions to reduce variance, with Random Forest as the key example. Boosting trains models sequentially where each corrects the previous one's errors to reduce bias, with XGBoost and AdaBoost as examples. Stacking trains a meta-model on base model outputs. Ensembles improve robustness and reduce both bias and variance.",
                "partial": "Ensemble learning combines multiple models to improve accuracy. Bagging trains in parallel and boosting trains sequentially. Random Forest and XGBoost are popular examples.",
                "incorrect": "Ensemble learning trains one large neural network using multiple GPU cards. It runs multiple datasets simultaneously on the same model to save training time."
            },
            {
                "correct": "Hyperparameters are configuration settings set before training that are not learned from data, such as learning rate, number of trees, max depth, batch size, and epochs. Hyperparameter tuning finds the optimal combination to maximise model performance. Grid Search exhaustively tests specified combinations. Random Search samples combinations more efficiently. Bayesian Optimisation uses past results to guide the search intelligently. Default values rarely produce the best performance.",
                "partial": "Hyperparameter tuning finds the best settings for a model that are configured before training. Grid search and random search are common techniques.",
                "incorrect": "Hyperparameter tuning adjusts model weights during training to reduce loss. It is the same as backpropagation and happens automatically."
            },
        ],
    },

    "Software Engineering": {

        "Easy": [
            {
                "correct": "The Software Development Life Cycle is a structured process used to design, develop, test, and deliver software systematically. Standard phases include Planning, Requirements Analysis, System Design, Implementation, Testing, Deployment, and Maintenance. SDLC improves project management, reduces risk, controls cost, and ensures the product meets user requirements. Common models include Waterfall, Agile, Spiral, and V-Model.",
                "partial": "SDLC guides software development through defined phases like planning, design, coding, testing, and deployment for organised delivery.",
                "incorrect": "SDLC is a programming language that automates software deployment. It stands for Software Debugging and Launching Cycle and is only for government projects."
            },
            {
                "correct": "Version control tracks and manages changes to files over time, enabling collaboration, rollback, and a complete history of modifications. It allows multiple developers to work without overwriting each other, provides an audit trail, enables rollback to stable versions when bugs appear, and supports branching for parallel feature development. Git is the most widely used version control system.",
                "partial": "Version control tracks code changes and allows multiple developers to collaborate. It lets you revert to previous versions if something breaks.",
                "incorrect": "Version control checks the operating system version before running software. It is only needed by large companies and unnecessary for small projects."
            },
            {
                "correct": "Git is a distributed version control system created by Linus Torvalds in 2005 that tracks source code changes and enables collaboration. Every developer has a complete local copy of the repository. Key concepts include repository, commit, branch, merge, pull request, clone, push, and pull. Git forms the foundation of platforms like GitHub, GitLab, and Bitbucket.",
                "partial": "Git is a version control system for tracking code changes and collaborating with other developers using commits, branches, and merges.",
                "incorrect": "Git is a cloud storage service for hosting websites. It is the same as GitHub and needs an internet connection to track local changes."
            },
            {
                "correct": "Debugging is the process of identifying, analysing, and fixing defects in software causing incorrect behaviour. It involves reproducing the bug, isolating its cause using logging, breakpoints, and print statements, and using debugger tools such as pdb in Python or browser DevTools. Effective debugging requires understanding code flow, reading error messages carefully, and systematically narrowing down the root cause.",
                "partial": "Debugging is finding and fixing errors in code. Tools like breakpoints and print statements help identify where the problem occurs.",
                "incorrect": "Debugging removes all comments and documentation from code to make it run faster. It is done automatically by the Python interpreter at runtime."
            },
            {
                "correct": "Software testing evaluates an application to identify defects and verify it meets requirements. Types include unit testing for individual components, integration testing for component interactions, system testing for the full application, and acceptance testing for user validation. Testing can be manual or automated. It ensures quality, reliability, and security before release while reducing the cost of late bug fixes.",
                "partial": "Software testing checks whether the application works correctly and meets requirements including unit, integration, and system testing.",
                "incorrect": "Software testing means writing code faster by skipping documentation. It is only done after deployment when users report issues."
            },
        ],

        "Medium": [
            {
                "correct": "REST is an architectural style for designing networked applications using standard HTTP methods to operate on resources identified by URLs. GET retrieves data, POST creates data, PUT or PATCH updates data, and DELETE removes data. Key principles include statelessness where each request is self-contained, resource-based URLs, standard HTTP status codes, and JSON as the typical data format. REST APIs are simple, scalable, and language-agnostic.",
                "partial": "A REST API uses HTTP methods like GET, POST, PUT, and DELETE to interact with resources. It is stateless and commonly uses JSON.",
                "incorrect": "A REST API connects two computers using Bluetooth. REST stands for Remote Execution and Storage Technology and is only used with Java."
            },
            {
                "correct": "Unit testing tests individual functions or methods in isolation to verify they produce correct output for given inputs. Dependencies are replaced with mocks or stubs to keep tests self-contained. Python frameworks include unittest and pytest. Unit tests are fast, deterministic, and precisely identify which function is broken, forming the foundation of a reliable test suite according to the testing pyramid.",
                "partial": "Unit testing tests individual functions in isolation to verify they work correctly. It uses frameworks like pytest and mocks to replace dependencies.",
                "incorrect": "Unit testing tests the entire application as one unit from the user's perspective. It is done manually by the QA team without writing code."
            },
            {
                "correct": "Integration testing verifies that multiple components work correctly when combined, testing interfaces and interactions between them. Examples include testing a service with a real database or an API communicating with a third-party service. It catches interface mismatches, data flow issues, and integration bugs that unit tests cannot detect. Integration tests are slower and more complex to set up than unit tests.",
                "partial": "Integration testing checks that different parts of the system work correctly together, such as a service and a database.",
                "incorrect": "Integration testing connects the software to the internet and tests download speeds. It is the same as unit testing but on a different operating system."
            },
            {
                "correct": "Agile is an iterative development methodology delivering software in small incremental cycles called sprints typically lasting one to four weeks. It emphasises collaboration between cross-functional teams and customers, responding to change over following a fixed plan, delivering working software frequently, and continuous improvement through retrospectives. Frameworks include Scrum, Kanban, and SAFe. It contrasts with Waterfall's rigid sequential process.",
                "partial": "Agile delivers software in short iterative sprints focusing on collaboration, flexibility, and continuous delivery of working software.",
                "incorrect": "Agile is a testing tool for running automated tests rapidly. It stands for Automated General Integration and Launching Engine and is a Python library."
            },
            {
                "correct": "Code review is the practice of having developers examine another developer's code before it is merged into the main codebase, typically through pull requests on GitHub. It catches bugs and logic errors early, enforces coding standards, spreads knowledge across the team reducing bus factor, improves code quality and maintainability, and provides learning opportunities for both author and reviewer.",
                "partial": "Code review is when another developer checks your code before it is merged. It helps catch bugs, improve quality, and share knowledge.",
                "incorrect": "Code review is an automated tool that checks variable name spelling. It is performed by the computer and involves no other developers."
            },
        ],

        "Hard": [
            {
                "correct": "Continuous Integration automatically builds and tests code on every developer push, catching integration issues early. Continuous Deployment automatically deploys every build passing all tests to production. Continuous Delivery keeps code deployable but requires manual release approval. A pipeline includes code commit trigger, automated build, unit and integration tests, security scanning, staging deployment, and production deployment. Common tools are Jenkins, GitHub Actions, and GitLab CI.",
                "partial": "CI automatically builds and tests code on every commit. CD automatically deploys passing builds to production. Together they speed up delivery and reduce manual errors.",
                "incorrect": "CI/CD stands for Client Integration and Customer Deployment. The client reviews code weekly and the developer deploys manually after approval."
            },
            {
                "correct": "Design patterns are reusable proven solutions to commonly occurring software design problems, not code but templates describing how to structure solutions. Creational patterns like Singleton, Factory, and Builder handle object creation. Structural patterns like Adapter and Decorator handle composition. Behavioural patterns like Observer and Strategy handle interaction. They provide shared vocabulary, speed development by reusing tested solutions, and improve maintainability.",
                "partial": "Design patterns are reusable solutions to common design problems categorised as creational, structural, and behavioural. Examples include Singleton, Factory, and Observer.",
                "incorrect": "Design patterns are UML diagrams that replace the need to write code. They only apply to Java and are not used in Python development."
            },
            {
                "correct": "Microservices architecture structures an application as small independently deployable services each responsible for a specific business capability communicating via REST APIs or messaging queues. Advantages include independent scaling, technology diversity, fault isolation, and faster deployment. Challenges include distributed systems complexity, network latency, cross-service data consistency, and high operational overhead requiring service discovery, API gateways, and distributed tracing.",
                "partial": "Microservices break an application into small independent services each handling one business function. They communicate via APIs and can be deployed independently.",
                "incorrect": "Microservices means writing Python functions shorter than ten lines each. Micro refers to file size and all services share the same database by default."
            },
            {
                "correct": "Dependency Injection is a design principle where an object receives its dependencies from an external source rather than creating them itself. Dependencies are injected through constructors, methods, or properties instead of being instantiated internally. Benefits include loose coupling, easier unit testing by allowing mock injection, better reusability, and adherence to the Dependency Inversion Principle. Frameworks like Spring in Java and dependency-injector in Python automate this.",
                "partial": "Dependency injection passes required objects into a class from outside rather than the class creating them, enabling loose coupling and easier testing.",
                "incorrect": "Dependency injection installs required libraries using pip. The program automatically downloads missing packages from the internet at runtime."
            },
            {
                "correct": "SOLID is a set of five principles for maintainable object-oriented design. Single Responsibility means a class has only one reason to change. Open/Closed means open for extension but closed for modification. Liskov Substitution means subclasses must be substitutable for parent classes without breaking the program. Interface Segregation means clients should not depend on interfaces they do not use. Dependency Inversion means high-level modules depend on abstractions not concrete implementations.",
                "partial": "SOLID stands for Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, and Dependency Inversion for clean object-oriented design.",
                "incorrect": "SOLID is a Python testing framework standing for Software Output and Logical Integrity Design used to validate machine learning model outputs."
            },
        ],
    },
}


def get_answers(domain: str, difficulty: str) -> List[AnswerSet]:
    if domain not in ANSWER_BANK:
        raise KeyError(f"Unknown domain: '{domain}'.")
    if difficulty not in ANSWER_BANK[domain]:
        raise KeyError(f"Unknown difficulty: '{difficulty}'.")
    return ANSWER_BANK[domain][difficulty]


def get_answer_set(domain: str, difficulty: str, index: int) -> AnswerSet:
    answers = get_answers(domain, difficulty)
    if index < 0 or index >= len(answers):
        raise IndexError(f"Index {index} out of range.")
    return answers[index]


def count_answer_sets() -> int:
    return sum(
        len(answer_list)
        for domain in ANSWER_BANK.values()
        for answer_list in domain.values()
    )


if __name__ == "__main__":
    total = count_answer_sets()
    print(f"Total answer sets : {total}")
    print(f"Total answers     : {total * 3}")