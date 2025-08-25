from app.db import Classroom, School, SessionLocal, UserAccount


def bootstrap():
    session = SessionLocal()

    school = School(name="School One")

    classroom1 = Classroom(name="Classroom One")
    classroom2 = Classroom(name="Classroom Two")

    school.classrooms.extend([classroom1, classroom2])

    teacher1 = UserAccount(
        name="Teacher One", email="t1@test.example", is_student=False
    )
    teacher2 = UserAccount(
        name="Teacher Two", email="t2@test.example", is_student=False
    )

    classroom1.user_accounts.append(teacher1)
    classroom2.user_accounts.append(teacher2)
    school.user_accounts.extend([teacher1, teacher2])

    for i in range(10):
        u1 = UserAccount(
            name=f"Classroom One Student {i}", email=f"s{i}c1@test.example"
        )
        u2 = UserAccount(
            name=f"Classroom Two Student {i}", email=f"s{i}c2@test.example"
        )
        classroom1.user_accounts.append(u1)
        classroom2.user_accounts.append(u2)
        school.user_accounts.extend([u1, u2])

    session.add_all([school, classroom1, classroom2])

    session.commit()


if __name__ == "__main__":
    bootstrap()
