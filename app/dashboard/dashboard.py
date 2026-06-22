from flask import Blueprint, render_template
from flask_login import login_required
from app.models import db, Order

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/')
def index():
    all_orders = db.session.query(Order).all()

    total_orders_count = len(all_orders)
    in_progress_count = len([o for o in all_orders if o.status == 'In progress'])
    completed_count = len([o for o in all_orders if o.status == 'Completed'])

    revenue = sum(o.total_cost for o in all_orders if o.status == 'Completed')

    return render_template(
        'dashboard/index.html',
        total_orders=total_orders_count,
        in_progress=in_progress_count,
        completed=completed_count,
        revenue=revenue,
        recent_orders=all_orders[:5])

