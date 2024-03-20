import streamlit as st
import random
import pandas as pd

def generate_random_numbers(start, end):
    numbers = list(range(start, end + 1))  # Generate the sequence from start to end
    random.shuffle(numbers)  # Shuffle the sequence randomly
    return numbers

def generate_random_teams(members, num_per_team):
    random.shuffle(members)
    teams = [members[i:i+num_per_team] for i in range(0, len(members), num_per_team)]
    return teams

def generate_random_projects(groups, has_titles, project_titles=None):
    random.shuffle(groups)
    if has_titles and project_titles:
        random.shuffle(project_titles)
        projects = {group: title for group, title in zip(groups, project_titles)}
    else:
        # Generate random numbers as project titles when no titles are provided.
        num_projects = len(groups)
        random_numbers = generate_random_numbers(1, num_projects)
        projects = {group: f"Project Title - {num}" for group, num in zip(groups, random_numbers)}
    return projects

def main():
    st.title("Randomizer App")

    option = st.sidebar.radio(
        "Select Option", ["Random Number", "Random Team Member", "Random Team Project"])

    if option == "Random Number":
        st.header("Random Number")
        start = st.number_input("Start Number", value=1)
        end = st.number_input("End Number", value=10)
        if start > end:
            st.error("Start number should be less than or equal to end number.")
        else:
            if st.button("Generate Random Numbers"):
                random_numbers = generate_random_numbers(start, end)
                st.write("Random Numbers:")
                for num in random_numbers:
                    st.write(num)

    elif option == "Random Team Member":
        st.header("Random Team Member per group")
        members = st.text_area("Enter Member Names (one per line)")
        num_per_team = st.number_input("Number of Members per Team", value=2)
        if st.button("Generate Teams"):
            members_list = members.split("\n")
            teams = generate_random_teams(members_list, num_per_team)
            st.write("Random Teams:")
            for i, team in enumerate(teams, 1):
                # Display each team as a table
                st.write(f"Team {i}:")
                team_df = pd.DataFrame({"No": [f"<div style='text-align:center'>{j}.</div>" for j in range(1, len(team) + 1)], 
                                        "Students": [f"<div style='text-align:center'>{student}</div>" for student in team]})
                st.write(team_df.to_html(index=False, escape=False), unsafe_allow_html=True)

    elif option == "Random Team Project":
        st.header("Random Team Project with title of project or exercise")
        groups = st.text_area("Enter Group Names or Numbers (one per line)")
        has_titles = st.radio("Do you have project titles?", ["Yes", "No"])
        if has_titles == "Yes":
            titles = st.text_area("Enter Project Titles (one per line)")
            project_titles = titles.split("\n")
        else:
            project_titles = None
        if st.button("Assign Projects"):
            groups_list = groups.split("\n")
            projects = generate_random_projects(groups_list, has_titles == "Yes", project_titles)
            st.write("Randomly Assigned Projects:")
            for group, project in projects.items():
                st.write(f"{group}: {project}")
    st.markdown("---")
    st.write("Project Holder by: OEUN PAO")
    st.write("Student of Department of Applied Mathematics and Statistics, ITC")
if __name__ == "__main__":
    main()
