# -*- coding: utf-8 -*-

from reimp import Blueprint, logger

bp = Blueprint('user')


@bp.route(101)
def login(request):
    request.write(dict(ret=101, body=repr(request.address)))

@bp.create_app_worker
def create_app_worker():
    logger.error('bp.create_app_worker')

@bp.create_app_conn
def create_app_conn(conn):
    logger.error('bp.create_app_conn')


@bp.close_app_conn
def close_app_conn(conn):
    logger.error('bp.close_app_conn')


@bp.before_app_first_request
def before_app_first_request(request):
    logger.error('bp.before_app_first_request')


@bp.before_app_request
def before_app_request(request):
    logger.error('bp.before_app_request')


@bp.after_app_request
def after_app_request(request, exc):
    logger.error('bp.after_app_request')


@bp.before_request
def before_request(request):
    logger.error('bp.before_request')


@bp.after_request
def after_request(request, exc):
    logger.error('bp.after_request')


@bp.before_app_response
def before_app_response(conn, rsp):
    logger.error('bp.before_app_response rsp: %r', rsp)


@bp.after_app_response
def after_app_response(conn, rsp, result):
    logger.error('bp.after_app_response rsp: %r, %s', rsp, result)


@bp.repeat_app_timer(5)
def repeat_app_timer():
    logger.error('bp.repeat_app_timer')
