from rest_framework import serializers

from api.models import Team, Match, Player, Goal


class PointTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('id', 'name', 'game_played', 'win', 'lost', 'draw', 'goal_fo', 'goal_against', 'point')


class MatchSerializer(serializers.ModelSerializer):
    team1 = serializers.SerializerMethodField('get_team_1_name')
    team2 = serializers.SerializerMethodField('get_team2_name')

    def get_team_1_name(self, obj):
        return obj.team1.name

    def get_team2_name(self, obj):
        return obj.team2.name

    class Meta:
        model = Match
        fields = ('id', 'team1', 'team2', 'date', 'match_status')


class PlayerSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField('get_image_url')
    player_category = serializers.SerializerMethodField('get_category')

    def get_image_url(self, obj):
        return obj.image.image_file.url

    def get_category(self, obj):
        return obj.category.name

    class Meta:
        model = Player
        fields = ('id', 'name', 'photo', 'no_of_goals', 'player_category')


class GoalSerializer(serializers.ModelSerializer):
    player_name = serializers.SerializerMethodField('get_player_name')

    def get_player_name(self, obj):
        return obj.player.name

    class Meta:
        model = Goal
        fields = ('id', 'name', 'photo', 'no_of_goals', 'player_category')
