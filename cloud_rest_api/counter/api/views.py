from rest_framework import status
from rest_framework.response import Response 
from rest_framework.decorators import api_view

from counter.models import Counter
from counter.api.serializers import CounterSerializer


# GET = get all counters (only one)
# POST = create new or reset existing counter
# PUT = update counter (number++)
@api_view(['GET','POST','PUT'])
def counter(request):
    try:
        if request.method == 'GET':
            counters = Counter.objects.all()
            serializer = CounterSerializer(counters, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            counters = Counter.objects.all()
            if len(counters) == 0:
                counter = Counter()
                counter.save()
                serializer = CounterSerializer(counter)
                return Response(serializer.data)
            else:
                counters[0].number = 0
                counters[0].save()
                serializer = CounterSerializer(counters[0])
                return Response(serializer.data)

        elif request.method == 'PUT':
            counters = Counter.objects.all()
            for c in counters:
                c.number += 1
                c.save()
            serializer = CounterSerializer(counters, many=True)
            return Response(serializer.data)

        else:
            return Response(status.HTTP_405_METHOD_NOT_ALLOWED)

    except Counter.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
