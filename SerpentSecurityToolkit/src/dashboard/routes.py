from flask import Blueprint, render_template

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/')
def home():
    return render_template('dashboard.html')

@dashboard_bp.route('/reconnaissance')
def reconnaissance():
    return render_template('reconnaissance.html')

@dashboard_bp.route('/network-scanner')
def network_scanner():
    return render_template('network_scanner.html')

@dashboard_bp.route('/log-analysis')
def log_analysis():
    return render_template('log_analysis.html')

@dashboard_bp.route('/messenger')
def messenger():
    return render_template('messenger.html')