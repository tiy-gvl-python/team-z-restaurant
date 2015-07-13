from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect


def get_request(*args, **kwargs):
    request = {}
    if "request" in kwargs:
        request = kwargs["request"]
    else:
        request = args[0]
    return request


def require_owner(view):
    def func(*args, **kwargs):
        request = get_request(*args, **kwargs)
        try:
            test = request.user.owner
            return view(*args, **kwargs)
        except ObjectDoesNotExist:
            return redirect("home")
        except AttributeError:
            return redirect("login")
    return func


def provide_customer(view):
    def func(*args, **kwargs):
        request = get_request(*args, **kwargs)
        try:
            cust_id = request.user.customer.id
            return view(pk=cust_id, *args, **kwargs)
        except ObjectDoesNotExist:
            return redirect("home")
        except AttributeError:
            return redirect("login")
    return func


def require_customer(view):
    def func(*args, **kwargs):
        request = get_request(*args, **kwargs)
        try:
            test = request.user.customer
            return view(*args, **kwargs)
        except ObjectDoesNotExist:
            return redirect("home")
        except AttributeError:
            return redirect("login")
    return func