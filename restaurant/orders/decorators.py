from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect


def require_owner(view):
    def func(*args, **kwargs):
        request = {}
        if "request" in kwargs:
            request = kwargs["request"]
        else:
            request = args[0]
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
        request = {}
        if "request" in kwargs:
            request = kwargs["request"]
        else:
            request = args[0]
        try:
            cust_id = request.user.customer.id
            return view(pk=cust_id, *args, **kwargs)
        except ObjectDoesNotExist:
            return redirect("home")
        except AttributeError:
            return redirect("login")
    return func