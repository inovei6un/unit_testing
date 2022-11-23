from unittest import TestCase, main

from some_projects.project_testing_library import Team


class TestTeam(TestCase):
    def setUp(self) -> None:
        self.team = Team('Team')

    def test_init(self):
        team_name = 'Team'
        team = Team(team_name)

        self.assertEqual(team_name, team.name)
        self.assertEqual({}, team.members)

    def test_name_setter_of_team_name(self):
        with self.assertRaises(ValueError) as context:
            Team('123asd123')

        self.assertEqual('Team Name can contain only letters!', str(context.exception))

    def test_add_member_adds_only_new_members_to_team(self):
        self.team.members['ivan'] = 18
        result = self.team.add_member(ivan=18, pesho=21, gosho=19, josh=16)

        self.assertEqual(f'Successfully added: pesho, gosho, josh', result)
        self.assertEqual(21, self.team.members['pesho'])
        self.assertEqual(19, self.team.members['gosho'])
        self.assertEqual(16, self.team.members['josh'])

    def test_remove_member_returns_error_when_player_does_not_exist(self):
        member_to_remove = 'Pesho'
        result = self.team.remove_member(member_to_remove)

        self.assertEqual(f"Member with name {member_to_remove} does not exist", result)

    def test_remove_member_when_member_exists(self):
        self.team.members['Pesho'] = 20
        self.team.members['Gosho'] = 12
        result = self.team.remove_member('Pesho')

        self.assertEqual(f"Member Pesho removed", result)
        self.assertEqual(12, self.team.members['Gosho'])
        self.assertTrue('Pesho' not in self.team.members)

    def test_team_greater_than_other_team(self):
        team_one = Team('Teamone')
        team_two = Team('Teamtwo')
        team_one.members['member1'] = 18
        team_one.members['member2'] = 19
        team_one.members['member3'] = 29

        team_two.members['member4'] = 24
        team_two.members['member5'] = 23

        self.assertEqual(True, team_one > team_two)
        self.assertEqual(False, team_two > team_one)

    def test_len_of_team_members(self):
        team_one = Team('Team')
        team_one.members['member1'] = 18
        team_one.members['member2'] = 19
        team_one.members['member3'] = 29
        result = len(team_one)

        self.assertEqual(3, result)

    def test_add_combining_two_teams(self):
        team_one = Team('Teamone')
        team_two = Team('Teamtwo')
        team_one.members['member1'] = 18
        team_one.members['member2'] = 19
        team_one.members['member3'] = 29

        team_two.members['member4'] = 24
        team_two.members['member5'] = 23

        result = team_one + team_two
        expected_result_members = {'member1': 18, 'member2': 19, 'member3': 29, 'member4': 24, 'member5': 23}
        self.assertEqual('TeamoneTeamtwo', result.name)

        self.assertEqual(expected_result_members, result.members)

    def test_str_returns_members_sorted_in_descending_order_by_age(self):
        team_one = Team('Teamone')
        team_one.members['member1'] = 18
        team_one.members['member2'] = 19
        team_one.members['member3'] = 29

        result = str(team_one)
        expected = f"Team name: Teamone\n" + \
                   f"Member: member3 - 29-years old\n" + \
                   f'Member: member2 - 19-years old\n' + \
                   f'Member: member1 - 18-years old'

        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
