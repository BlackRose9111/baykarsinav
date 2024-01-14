from django.contrib.auth import authenticate
from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from rest_framework import response as RestResponse
from rest_framework.decorators import api_view
from . import models, serializers,auth
from django.contrib.auth.models import User


def api_home(request, *args, **kwargs):
    return JsonResponse({"name": "UAVRent API", "version": "0.0.1"})



@api_view(["GET"])
def get_all(request):
    all_uavs = models.UAV.objects.all()
    serializer = serializers.UavSerializer(all_uavs, many=True)
    return RestResponse.Response(serializer.data)


@api_view(["GET", "POST", "PUT", "DELETE"])
def uav(request, *args, **kwargs):
    #get can be used for listing all without parameters or by id
    params = request.query_params
    print(params)
    if request.method == "GET":
        try:

            #get by id
            uav = models.UAV.objects.get(id=params.get("id"))
            serializer = serializers.UavSerializer(uav)
            return RestResponse.Response(serializer.data)
        except:

            #list all
            uavs = models.UAV.objects.all()
            serializer = serializers.UavSerializer(uavs, many=True)
            return RestResponse.Response(serializer.data)

    #post can be used for creating new
    elif request.method == "POST":
        data = request.data
        serializer = serializers.UavSerializerWithCategoryAsPrimaryKey(data=data)
        if serializer.is_valid():
            serializer.save()
            return RestResponse.Response(serializer.data)
        else:
            return RestResponse.Response(serializer.errors)

    #put can be used for updating existing
    elif request.method == "PUT":
        uav = models.UAV.objects.get(id=params.get("id"))
        #edit the uav
        serializer = serializers.UavSerializerWithCategoryAsPrimaryKey(uav, data=request.data)

        if serializer.is_valid():

            print(serializer.validated_data)
            print(request.data)
            serializer.save()
            return RestResponse.Response(serializer.data)
        else:
            return RestResponse.Response(serializer.errors)

    #delete can be used for deleting existing
    elif request.method == "DELETE":
        try:
            uav = models.UAV.objects.get(id=params.get("id"))
        except:
            return RestResponse.Response({"message": "UAV not found."})
        uav.delete()
        return RestResponse.Response({"message": "UAV deleted."})

    else:
        return RestResponse.Response({"message": "Method not allowed."})


@api_view(["GET", "POST", "PUT", "DELETE"])
def uav_category(request, *args, **kwargs):
    #get can be used for listing all without parameters or by id
    params = request.query_params
    if request.method == "GET":
        try:
            #get by id
            uav_category = models.UAVCategory.objects.get(id=params.get("id"))
            serializer = serializers.UavCategorySerializer(uav_category)
            return RestResponse.Response(serializer.data)
        except:
            #list all
            uav_categories = models.UAVCategory.objects.all()
            serializer = serializers.UavCategorySerializer(uav_categories, many=True)
            return RestResponse.Response(serializer.data)

    #post can be used for creating new
    elif request.method == "POST":
        serializer = serializers.UavCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return RestResponse.Response(serializer.data)
        else:
            return RestResponse.Response(serializer.errors)

    #put can be used for updating existing
    elif request.method == "PUT":
        uav_category = models.UAVCategory.objects.get(id=kwargs.get("id"))
        serializer = serializers.UavCategorySerializer(uav_category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return RestResponse.Response(serializer.data)
        else:
            return RestResponse.Response(serializer.errors)

    #delete can be used for deleting existing
    elif request.method == "DELETE":
        uav_category = models.UAVCategory.objects.get(id=kwargs.get("id"))
        uav_category.delete()
        return RestResponse.Response({"message": "UAV category deleted."})

    else:
        return RestResponse.Response({"message": "Method not allowed."})

@api_view(["GET"])
def search_uav(request, *args, **kwargs):
    #model, manufacturer, category, price. We query using AND logic, as in all parameters must be met. All parameters are optional, however.
    params = request.GET
    print(params)
    uavs = models.UAV.objects.filter()
    return RestResponse.Response({"message": "Not implemented yet."})



#We can use Match Case to replace the if-else statements if we fancy and if we are using Python 3.10
@api_view(["GET", "POST", "PUT", "DELETE"])
def rent(request, *args, **kwargs):
    params = request.query_params
    match request.method:
        case "GET":
            try:
                rent = models.Rent.objects.get(id=params.get("id"))
                serializer = serializers.RentSerializer(rent)
                return RestResponse.Response(serializer.data)
            except Exception as e:
                rents = models.Rent.objects.all()
                serializer = serializers.RentSerializer(rents, many=True)
                return RestResponse.Response(serializer.data)
        case "POST":
            serializer = serializers.RentSerializerWithPrimaryKey(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return RestResponse.Response(serializer.data)
            else:
                return RestResponse.Response(serializer.errors)
        case "PUT":
            rent = models.Rent.objects.get(id=params.get("id"))
            serializer = serializers.RentSerializerWithPrimaryKey(rent, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return RestResponse.Response(serializer.data)
            else:
                return RestResponse.Response(serializer.errors)
        case "DELETE":
            rent = models.Rent.objects.get(id=params.get("id"))
            rent.delete()
            return RestResponse.Response({"message": "Rent deleted."})
        case _:
            return RestResponse.Response({"message": "Method not allowed."})


@api_view(["GET"])
def filter_rent(request):
    #filter by user, uav, start date, end date
    query_params = request.query_params
    from django.db.models import Q
    username = query_params.get("username")
    uav_name = query_params.get("uav_name")
    start_date = query_params.get("start_date")
    end_date = query_params.get("end_date")
    filter_name_query = Q()
    filter_query = Q()
    if username is not None:
        filter_query = filter_name_query & Q(renter__username=username)
    if uav_name is not None:
        filter_query = filter_name_query | Q(uav__name=uav_name)
    filter_query = filter_query & filter_name_query
    if start_date is not None:
        filter_query = filter_query & Q(start_date__gte=start_date)
    if end_date is not None:
        filter_query = filter_query & Q(end_date__lte=end_date)
    rents = models.Rent.objects.filter(filter_query)
    serializer = serializers.RentSerializer(rents, many=True)
    return RestResponse.Response(serializer.data)









@api_view(["GET"])
def user(request):
    #get all users
    users = User.objects.all()
    serializer = serializers.UserSerializer(users, many=True)
    return RestResponse.Response(serializer.data)




@api_view(["POST"])
def register(request):
    serializer = serializers.UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return RestResponse.Response(serializer.data)
    else:
        return RestResponse.Response(serializer.errors)


@api_view(["POST"])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(username=username, password=password)
    if user is not None:
        token = auth.generate_jwt_token(user)
        return RestResponse.Response({"token": token})
    else:
        return RestResponse.Response({"message": "Invalid credentials."})


@api_view(["GET"])
def get_my_rentals(request):
    token = request.headers.get("Authorization")
    if token is None:
        return RestResponse.Response({"message": "Not authorized."})
    user_id = auth.extract_user(token)
    if user_id is None:
        return RestResponse.Response({"message": "Not authorized."})
    user = User.objects.get(id=user_id)
    rents = models.Rent.objects.filter(renter=user)
    serializer = serializers.RentSerializer(rents, many=True)
    return RestResponse.Response(serializer.data)


@api_view(["GET"])
def get_my_user(request):
    #find user from the auth toke
    token = request.headers.get("Authorization")
    if token is None:
        return RestResponse.Response({"message": "Not authorized."})
    user_id = auth.extract_user(token)
    if user_id is None:
        return RestResponse.Response({"message": "Not authorized."})
    user = User.objects.get(id=user_id)
    serializer = serializers.UserSerializer(user)
    return RestResponse.Response(serializer.data)










