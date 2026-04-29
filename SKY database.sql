
PRAGMA foreign_keys = ON;


-- Table: AuditLog
CREATE TABLE IF NOT EXISTS AuditLog (
    audit_id INTEGER PRIMARY KEY,
    entity_name TEXT NOT NULL,
    action TEXT NOT NULL,
    timestamp TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES User(user_id)
);

-- Table: Department
CREATE TABLE IF NOT EXISTS Department (
    department_id INTEGER PRIMARY KEY,
    department_name TEXT NOT NULL,
    department_head_id INTEGER NOT NULL,
    organisation_id INTEGER NOT NULL,
    FOREIGN KEY (department_head_id) REFERENCES User(user_id),
    FOREIGN KEY (organisation_id) REFERENCES Organisation(organisation_id)
);

-- Table: DeptContactChannel
CREATE TABLE IF NOT EXISTS DeptContactChannel (
    dept_channel_id INTEGER PRIMARY KEY,
    typeofcontactchannel TEXT NOT NULL,
    contact_channel_link TEXT NOT NULL,
    department_id INTEGER NOT NULL,
    FOREIGN KEY (department_id) REFERENCES Department(department_id)
);

-- Table: Meeting
CREATE TABLE IF NOT EXISTS Meeting (
    meeting_id INTEGER PRIMARY KEY,
    meeting_date TEXT NOT NULL,
    meeting_msgs TEXT NOT NULL,
    team_id INTEGER NOT NULL,
    created_by_user_id INTEGER NOT NULL,
    FOREIGN KEY (team_id) REFERENCES Team(team_id),
    FOREIGN KEY (created_by_user_id) REFERENCES User(user_id)
);

-- Table: Message
CREATE TABLE IF NOT EXISTS Message (
    message_id INTEGER PRIMARY KEY,
    subject TEXT NOT NULL,
    content TEXT NOT NULL,
    time_created TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    message_status TEXT NOT NULL,
    user_id INTEGER NOT NULL,
    team_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES User(user_id),
    FOREIGN KEY (team_id) REFERENCES Team(team_id)
);

-- Table: Organisation
CREATE TABLE IF NOT EXISTS Organisation (
    organisation_id INTEGER PRIMARY KEY,
    organisationName TEXT NOT NULL,
    organisationDescription TEXT
);

-- Table: Project
CREATE TABLE IF NOT EXISTS Project (
    project_id INTEGER PRIMARY KEY,
    project_name TEXT NOT NULL,
    board_link TEXT NOT NULL,
    team_id INTEGER NOT NULL,
    FOREIGN KEY (team_id) REFERENCES Team(team_id)
);

-- Table: Repository
CREATE TABLE IF NOT EXISTS Repository (
    repo_id INTEGER PRIMARY KEY,
    repo_name TEXT NOT NULL,
    repo_url TEXT NOT NULL,
    repo_site TEXT NOT NULL,
    team_id INTEGER NOT NULL,
    project_id INTEGER NOT NULL,
    FOREIGN KEY (team_id) REFERENCES Team(team_id),
    FOREIGN KEY (project_id) REFERENCES Project(project_id)
);

-- Table: Team
CREATE TABLE IF NOT EXISTS Team (
    team_id INTEGER PRIMARY KEY,
    team_name TEXT NOT NULL,
    team_goal TEXT,
    team_wiki TEXT,
    development_focus_areas TEXT,
    key_skills_technologies TEXT,
    manager_id INTEGER NOT NULL,
    department_id INTEGER NOT NULL,
    FOREIGN KEY (manager_id) REFERENCES User(user_id),
    FOREIGN KEY (department_id) REFERENCES Department(department_id)
);

-- Table: TeamContactChannel
CREATE TABLE IF NOT EXISTS TeamContactChannel (
    team_channel_id INTEGER PRIMARY KEY,
    typeofcontactchannel TEXT NOT NULL,
    contact_channel_link TEXT NOT NULL,
    team_id INTEGER NOT NULL,
    FOREIGN KEY (team_id) REFERENCES Team(team_id)
);

-- Table: TeamDependency
CREATE TABLE IF NOT EXISTS TeamDependency (
    team_dependency_id INTEGER PRIMARY KEY,
    dependency_type TEXT NOT NULL,
    team_id INTEGER NOT NULL,
    dependency_team_id INTEGER NOT NULL,
    FOREIGN KEY (team_id) REFERENCES Team(team_id),
    FOREIGN KEY (dependency_team_id) REFERENCES Team(team_id)
);

-- Table: TeamMember
CREATE TABLE IF NOT EXISTS TeamMember (
    member_id INTEGER PRIMARY KEY,
    team_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (team_id) REFERENCES Team(team_id),
    FOREIGN KEY (user_id) REFERENCES User(user_id)
);

-- Table: User
CREATE TABLE IF NOT EXISTS User (
    user_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    username TEXT NOT NULL UNIQUE,
    user_email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    is_admin INTEGER NOT NULL DEFAULT 0
);

