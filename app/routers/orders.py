from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models import db, Order, User

orders_bp = Blueprint('orders', __name__, url_prefix='/orders')

@orders_bp.route('/')
@login_required
def list_orders():
    search_query = request.args.get('search', '').strip()
    status_filter = request.args.get('status', '').strip()
    
    query = db.session.query(Order)
    
    if search_query:
        query = query.filter(
            (Order.client_name.ilike(f"%{search_query}%")) | 
            (Order.product.ilike(f"%{search_query}%"))
        )
        
    if status_filter:
        query = query.filter(Order.status == status_filter)
        
    orders = query.order_by(Order.created_at.desc()).all()
    
    return render_template('orders/list.html', orders=orders, search=search_query, status_filter=status_filter)

@orders_bp.route('/add', methods=['GET', 'POST'])
@login_required
def add_order():
    if request.method == 'POST':
        client_name = request.form.get('client_name')
        product = request.form.get('product')
        quantity = request.form.get('quantity', type=int)
        price = request.form.get('price', type=float)
        
        if not client_name or not product or not quantity or not price:
            flash('Please fill in all the fields correctly!', 'danger')
            return redirect(url_for('orders.add_order'))
            
        new_order = Order(
            client_name=client_name,
            product=product,
            quantity=quantity,
            price=price,
            user_id=current_user.id
        )
        
        db.session.add(new_order)
        db.session.commit()
        
        flash('The order has been successfully created!', 'success')
        return redirect(url_for('orders.list_orders'))
        
    return render_template('orders/form.html', action="Добавить")

@orders_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_order(id):
    order = db.session.get(Order, id)
    if not order:
        flash('Order not found.', 'danger')
        return redirect(url_for('orders.list_orders'))
        
    if request.method == 'POST':
        order.client_name = request.form.get('client_name')
        order.product = request.form.get('product')
        order.quantity = request.form.get('quantity', type=int)
        order.price = request.form.get('price', type=float)
        order.status = request.form.get('status')
        
        db.session.commit()
        flash('Order updated successfully!', 'success')
        return redirect(url_for('orders.list_orders'))
        
    return render_template('orders/form.html', order=order, action="Edit")

@orders_bp.route('/status/<int:id>/<string:new_status>')
@login_required
def update_status(id, new_status):
    order = db.session.get(Order, id)
    if not order:
        flash('Order not found.', 'danger')
        return redirect(url_for('orders.list_orders'))
        
    if new_status in ['New', 'In progress', 'Completed']:
        order.status = new_status
        db.session.commit()
        flash(f'Order #{id} status has been successfully changed to "{new_status}"', 'success')
    else:
        flash('Invalid order status.', 'danger')
        
    return redirect(url_for('orders.list_orders'))

@orders_bp.route('/delete/<int:id>')
@login_required
def delete_order(id):
    if current_user.role != 'admin':
        flash('You dont have permission to do this!', 'danger')
        return redirect(url_for('orders.list_orders'))
        
    order = db.session.get(Order, id)
    if not order:
        flash('Order not found.', 'danger')
        return redirect(url_for('orders.list_orders'))
        
    db.session.delete(order)
    db.session.commit()
    
    flash(f'Order #{id} has been successfully deleted.', 'success')
    return redirect(url_for('orders.list_orders'))

