from softball import app, db


class stats(db.Model):
    """
    Table structure
    """
    __tablename__ = 'stats'
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    date = db.Column(db.String(50))
    team = db.Column(db.String(50))
    league_name = db.Column(db.String(50))
    league_type = db.Column(db.String(50))
    game_type = db.Column(db.String(50))
    field = db.Column(db.Integer)
    outcome = db.Column(db.String(5))
    at_bats = db.Column(db.Integer)
    hits = db.Column(db.Integer)
    runs = db.Column(db.Integer)
    walks = db.Column(db.Integer)
    singles = db.Column(db.Integer)
    doubles = db.Column(db.Integer)
    triples = db.Column(db.Integer)
    four_baggers = db.Column(db.Integer)
    home_runs = db.Column(db.Integer)
    dead_ball_outs = db.Column(db.Integer)
    runs_batted_in = db.Column(db.Integer)
    ball_type = db.Column(db.String(50))
    bat_used = db.Column(db.String(50))

    def __repr__(self):
        return '<stats %r>' % self.id

    def to_json(self):
        return {
            "id": self.id,
            "date": self.date,
            "team": self.team,
            "league_name": self.league_name,
            "league_type": self.league_type,
            "game_type": self.game_type,
            "field": self.field,
            "outcome": self.outcome,
            "at_bats": self.at_bats,
            "hits": self.hits,
            "runs": self.runs,
            "walks": self.walks,
            "singles": self.singles,
            "doubles": self.doubles,
            "triples": self.triples,
            "four_baggers": self.four_baggers,
            "home_runs": self.home_runs,
            "dead_ball_outs": self.dead_ball_outs,
            "runs_batted_in": self.runs_batted_in,
            "ball_type": self.doubles,
            "bat_used": self.triples
            }

    def from_json(self, source):
        for key in ["id", "date", "team", "league_name", "league_type", "game_type", "field", "outcome", "at_bats",
                    "hits", "runs", "walks", "singles", "doubles", "triples", "four_baggers", "home_runs",
                    "dead_ball_outs","runs_batted_in","ball_type","bat_used"]:
            if key in source:
                setattr(self, key, source[key])
            else:
                setattr(self, key, None)



