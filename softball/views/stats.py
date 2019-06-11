
from softball import app, db
from softball.models import stats as mstats
from flask import Flask, Response, request, json, jsonify, url_for, g, _request_ctx_stack, abort, has_request_context, session, make_response, send_file
from flask import Blueprint
import time
from datetime import datetime


mod = Blueprint('stats', __name__, url_prefix='/stats')

#stats/add
@mod.route('/add', methods=['POST'])
#@ma.login_required
#@authtest()
def stats_add():
    #d = GetLogInfo(request)
    #app.logger.info('%s %r', "Entering view, user PUT data:", request.get_json(), extra=d)

    r = request.get_json()
    stat = mstats.stats()
    stat.from_json(r)
    db.session.add(stat)
    db.session.commit()
    result = stat.to_json()
    app.logger.info('%s %r', "Successfully added new record to database:", result)
    return "200"


#stats/delete
@mod.route('/deletebyid', methods=['GET', 'PUT'])
@mod.route('/delete', methods=['GET', 'PUT'])
#@ma.login_required
#@authtest()
def stats_delete():
    #d = GetLogInfo(request)
    #app.logger.info('%s', "Entering view...", extra=d)

    r = request.get_json()
    if r.has_key('id'):
        stat = mstats.stats.query.filter_by(id=r['id'])
    else:
        app.logger.info('%s', "Exited, need rackunit to delete.")
        return "409"
    if stat.first() is None:
        app.logger.info('%s', "Exited, record not found in database.")
        return "404"

    # Display the record to be deleted
    deleted_record = stat.first().to_json()

    stat.delete()
    db.session.commit()
    app.logger.info('%s %r', "Successfully deleted record from database:", deleted_record)
    return "200"


#stat/get
@mod.route('/get', methods=['GET', 'PUT'])
#@ma.login_required
#@authtest()
def stats_get():
    #d = GetLogInfo(request)
    #app.logger.info('%s %r', "Entering view, user PUT data:", request.get_json(), extra=d)

    rebuiltjson = {}
    for key, value in request.get_json().iteritems():
        for keyname in ["id", "date", "team", "league_name", "league_type", "game_type", "field", "outcome", "at_bats",
                        "hits", "runs", "walks", "singles", "doubles", "triples", "four_baggers", "home_runs",
                        "dead_ball_outs","runs_batted_in","ball_type","bat_used"]:
            if key == keyname:
                rebuiltjson[keyname] = value

    if len(rebuiltjson) == 0:
        app.logger.info('%s', "Exited, user provides no search data.")
        return "400"

    stat = mstats.stats.query.filter_by(**rebuiltjson).all()
    result = [mstats.stats.to_json(x) for x in stat]

    app.logger.info('%s', "Call to get succeeded.")
    return "200"


#stats/list
@mod.route('/list')
#@ma.login_required
#@authtest()
def stats_list():
    #d = GetLogInfo(request)
    #app.logger.info('%s', "Entering view...", extra=d)

    stat = mstats.stats.query.all()
    result = [mstats.stats.to_json(x) for x in stat]

    app.logger.info('%s', "Call to list succeeded.")
    return "200"


#stats/update
@mod.route('/updatebyid', methods=['PUT'])
@mod.route('/update', methods=['PUT'])
#@ma.login_required
#@authtest()
def stats_update():
    #d = GetLogInfo(request)
    #app.logger.info('%s %r', "Entering view, user PUT data:", request.get_json(), extra=d)

    r = request.get_json()
    if r.has_key('id'):
        stat = mstats.stats.query.filter_by(id=r['id']).first()
    else:
        app.logger.info('%s', "Exited, need rackunit or id to update.")
        return "400"

    if stat is None:
        app.logger.info('%s', "Exited, record not found in database.")
        return "404"

    for key, value in r.iteritems():
        stat[key] = value

    db.session.commit()
    app.logger.info('%s %r', "Successfully updated record in database:",stat.to_json())
    return "200"
