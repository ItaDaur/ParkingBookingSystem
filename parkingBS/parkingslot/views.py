import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ParkingSlot
from .form import CreateParkingSlotForm, UpdateParkingSlotForm

# For Customer

# create a slot
def create_slot(request):
    if request.method == 'POST':
        form = CreateParkingSlotForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.created_by = request.user
            var.slot_status = 'Pending'
            var.save()
            messages.info(request, 'Your parking slot has been successfully submitted. An engineer would be assigned soon.')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Something went wrong. Please check form input')
            return redirect('create-slot')
    else:
        form = CreateParkingSlotForm()
        content = {'form': form}
        return render(request, 'parkingslot/create_slot.html', content)

# update a slot
def update_slot(request, pk):
    slot = ParkingSlot.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateParkingSlotForm(request.POST, instance=slot)
        if form.is_valid():
            form.save()
            messages.info(request, 'Your slot info has been updated and all the changes are saved in the Database')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Something went wrong. Please check form input')
            # return redirect('create-slot')
    else:
        form = UpdateParkingSlotForm(instance=slot)
        content = {'form': form}
        return render(request, 'parkingslot/update_slot.html', content)

#   viewing all created slots
def all_slots(request):
    slots = ParkingSlot.objects.filter(created_by=request.user)
    content = {'slots': slots}
    return render(request, 'parkingslot/all_slots.html', content)

# view slot details
def slot_details(request, pk):
    slot = ParkingSlot.objects.get(pk=pk)
    content = {'slot': slot}
    return render(request, 'parkingslot/slot_details.html', content)

# Engineering
# view slot queue
def slot_queue(request):
    slots = ParkingSlot.objects.filter(slot_status='Pending')
    content = {'slots': slots}
    return render(request, 'parkingslot/slot_queue.html', content)

# accept a slot from the queue
def accept_slot(request, pk):
    slot = ParkingSlot.objects.get(pk=pk)
    slot.assigned_to = request.user
    slot.slot_status = 'Active'
    slot.accepted_date = datetime.datetime.now()
    slot.save()
    messages.info(request, 'Slot has been accepted. Please resolve as soon as possible!')
    return redirect('slot-queue')

# close a slot
def close_slot(request, pk):
    slot = ParkingSlot.objects.get(pk=pk)
    slot.slot_status = 'Completed'
    slot.is_resolved = True
    slot.accepted_date = datetime.datetime.now()
    slot.save()
    messages.info(request, 'Slot has been resolved. Thank you brilliant Support Engineer!')
    return redirect('slot-queue')

# slots engineer is working on
def workspace(request):
    slots = ParkingSlot.objects.filter(assigned_to=request.user, is_resolved=False)
    content = {'slots': slots}
    return render(request, 'parkingslot/workspace.html', content)

# all closed/resolved slots
def all_closed_slots(request):
    slots = ParkingSlot.objects.filter(assigned_to=request.user, is_resolved=True)
    content = {'slots': slots}
    return render(request, 'parkingslot/all_closed_slots.html', content)


