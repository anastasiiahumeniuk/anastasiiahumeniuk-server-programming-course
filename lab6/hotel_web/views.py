from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from hotel_management.models import *
from django.urls import reverse_lazy

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from colleague_project.core.models import Customer

class IndexView(TemplateView):
    template_name = 'hotel_web/index.html'

class GuestListView(ListView):
    model = Guest
    template_name = 'hotel_web/guest_list.html'
    context_object_name = 'guests'

class GuestDetailView(DetailView):
    model = Guest
    template_name = 'hotel_web/guest_detail.html'

class GuestCreateView(CreateView):
    model = Guest
    fields = ['first_name','last_name','email','phone_number','passport_series','passport_number','date_of_birth']
    template_name = 'hotel_web/guest_form.html'
    success_url = reverse_lazy('hotel_web:guest_list')

class GuestUpdateView(UpdateView):
    model = Guest
    fields = ['first_name','last_name','email','phone_number','passport_series','passport_number','date_of_birth']
    template_name = 'hotel_web/guest_form.html'
    success_url = reverse_lazy('hotel_web:guest_list')

class GuestDeleteView(DeleteView):
    model = Guest
    template_name = 'hotel_web/guest_confirm_delete.html'
    success_url = reverse_lazy('hotel_web:guest_list')


class RoomTypeListView(ListView):
    model = RoomType
    template_name = 'hotel_web/roomtype_list.html'
    context_object_name = 'roomtypes'

class RoomTypeDetailView(DetailView):
    model = RoomType
    template_name = 'hotel_web/roomtype_detail.html'

class RoomTypeCreateView(CreateView):
    model = RoomType
    fields = ['name','description','base_price']
    template_name = 'hotel_web/roomtype_form.html'
    success_url = reverse_lazy('hotel_web:roomtype_list')

class RoomTypeUpdateView(UpdateView):
    model = RoomType
    fields = ['name','description','base_price']
    template_name = 'hotel_web/roomtype_form.html'
    success_url = reverse_lazy('hotel_web:roomtype_list')

class RoomTypeDeleteView(DeleteView):
    model = RoomType
    template_name = 'hotel_web/roomtype_confirm_delete.html'
    success_url = reverse_lazy('hotel_web:roomtype_list')

class RoomListView(ListView):
    model = Room
    template_name = 'hotel_web/room_list.html'
    context_object_name = 'rooms'

class RoomDetailView(DetailView):
    model = Room
    template_name = 'hotel_web/room_detail.html'

class RoomCreateView(CreateView):
    model = Room
    fields = ['room_number','room_type','floor_number','capacity','price_per_night','status','description']
    template_name = 'hotel_web/room_form.html'
    success_url = reverse_lazy('hotel_web:room_list')

class RoomUpdateView(UpdateView):
    model = Room
    fields = ['room_number','room_type','floor_number','capacity','price_per_night','status','description']
    template_name = 'hotel_web/room_form.html'
    success_url = reverse_lazy('hotel_web:room_list')

class RoomDeleteView(DeleteView):
    model = Room
    template_name = 'hotel_web/room_confirm_delete.html'
    success_url = reverse_lazy('hotel_web:room_list')

class ServiceCategoryListView(ListView):
    model = ServiceCategory
    template_name = 'hotel_web/servicecategory_list.html'
    context_object_name = 'categories'

class ServiceCategoryDetailView(DetailView):
    model = ServiceCategory
    template_name = 'hotel_web/servicecategory_detail.html'

class ServiceCategoryCreateView(CreateView):
    model = ServiceCategory
    fields = ['name']
    template_name = 'hotel_web/servicecategory_form.html'
    success_url = reverse_lazy('hotel_web:servicecategory_list')

class ServiceCategoryUpdateView(UpdateView):
    model = ServiceCategory
    fields = ['name']
    template_name = 'hotel_web/servicecategory_form.html'
    success_url = reverse_lazy('hotel_web:servicecategory_list')

class ServiceCategoryDeleteView(DeleteView):
    model = ServiceCategory
    template_name = 'hotel_web/servicecategory_confirm_delete.html'
    success_url = reverse_lazy('hotel_web:servicecategory_list')

class ServiceListView(ListView):
    model = Service
    template_name = 'hotel_web/service_list.html'
    context_object_name = 'services'

class ServiceDetailView(DetailView):
    model = Service
    template_name = 'hotel_web/service_detail.html'

class ServiceCreateView(CreateView):
    model = Service
    fields = ['service_name','price','service_description','service_category']
    template_name = 'hotel_web/service_form.html'
    success_url = reverse_lazy('hotel_web:service_list')

class ServiceUpdateView(UpdateView):
    model = Service
    fields = ['service_name','price','service_description','service_category']
    template_name = 'hotel_web/service_form.html'
    success_url = reverse_lazy('hotel_web:service_list')

class ServiceDeleteView(DeleteView):
    model = Service
    template_name = 'hotel_web/service_confirm_delete.html'
    success_url = reverse_lazy('hotel_web:service_list')

class BookingListView(ListView):
    model = Booking
    template_name = 'hotel_web/booking_list.html'
    context_object_name = 'bookings'

class BookingDetailView(DetailView):
    model = Booking
    template_name = 'hotel_web/booking_detail.html'

class BookingCreateView(CreateView):
    model = Booking
    fields = ['guest','room','check_in_date','check_out_date','booking_status','services']
    template_name = 'hotel_web/booking_form.html'
    success_url = reverse_lazy('hotel_web:booking_list')

class BookingUpdateView(UpdateView):
    model = Booking
    fields = ['guest','room','check_in_date','check_out_date','booking_status','services']
    template_name = 'hotel_web/booking_form.html'
    success_url = reverse_lazy('hotel_web:booking_list')

class BookingDeleteView(DeleteView):
    model = Booking
    template_name = 'hotel_web/booking_confirm_delete.html'
    success_url = reverse_lazy('hotel_web:booking_list')

class PaymentListView(ListView):
    model = Payment
    template_name = 'hotel_web/payment_list.html'
    context_object_name = 'payments'

class PaymentDetailView(DetailView):
    model = Payment
    template_name = 'hotel_web/payment_detail.html'

class PaymentCreateView(CreateView):
    model = Payment
    fields = ['booking','payment_date','amount','payment_method','payment_status','partial_payment']
    template_name = 'hotel_web/payment_form.html'
    success_url = reverse_lazy('hotel_web:payment_list')

class PaymentUpdateView(UpdateView):
    model = Payment
    fields = ['booking','payment_date','amount','payment_method','payment_status','partial_payment']
    template_name = 'hotel_web/payment_form.html'
    success_url = reverse_lazy('hotel_web:payment_list')

class PaymentDeleteView(DeleteView):
    model = Payment
    template_name = 'hotel_web/payment_confirm_delete.html'
    success_url = reverse_lazy('hotel_web:payment_list')

class FeedbackListView(ListView):
    model = Feedback
    template_name = 'hotel_web/feedback_list.html'
    context_object_name = 'feedbacks'

class FeedbackDetailView(DetailView):
    model = Feedback
    template_name = 'hotel_web/feedback_detail.html'

class FeedbackCreateView(CreateView):
    model = Feedback
    fields = ['guest','booking','rating','title','comment','is_public']
    template_name = 'hotel_web/feedback_form.html'
    success_url = reverse_lazy('hotel_web:feedback_list')

class FeedbackUpdateView(UpdateView):
    model = Feedback
    fields = ['guest','booking','rating','title','comment','is_public']
    template_name = 'hotel_web/feedback_form.html'
    success_url = reverse_lazy('hotel_web:feedback_list')

class FeedbackDeleteView(DeleteView):
    model = Feedback
    template_name = 'hotel_web/feedback_confirm_delete.html'
    success_url = reverse_lazy('hotel_web:feedback_list')

class RoomMaintenanceListView(ListView):
    model = RoomMaintenance
    template_name = 'hotel_web/roommaintenance_list.html'
    context_object_name = 'maintenances'

class RoomMaintenanceDetailView(DetailView):
    model = RoomMaintenance
    template_name = 'hotel_web/roommaintenance_detail.html'

class RoomMaintenanceCreateView(CreateView):
    model = RoomMaintenance
    fields = ['room','start_date','end_date','description','maintenance_type']
    template_name = 'hotel_web/roommaintenance_form.html'
    success_url = reverse_lazy('hotel_web:roommaintenance_list')

class RoomMaintenanceUpdateView(UpdateView):
    model = RoomMaintenance
    fields = ['room','start_date','end_date','description','maintenance_type']
    template_name = 'hotel_web/roommaintenance_form.html'
    success_url = reverse_lazy('hotel_web:roommaintenance_list')

class RoomMaintenanceDeleteView(DeleteView):
    model = RoomMaintenance
    template_name = 'hotel_web/roommaintenance_confirm_delete.html'
    success_url = reverse_lazy('hotel_web:roommaintenance_list')


class BookingLogListView(ListView):
    model = BookingLog
    template_name = 'hotel_web/bookinglog_list.html'
    context_object_name = 'logs'

class BookingLogDetailView(DetailView):
    model = BookingLog
    template_name = 'hotel_web/bookinglog_detail.html'

class BookingLogCreateView(CreateView):
    model = BookingLog
    fields = ['booking','old_status','new_status']
    template_name = 'hotel_web/bookinglog_form.html'
    success_url = reverse_lazy('hotel_web:bookinglog_list')

class BookingLogUpdateView(UpdateView):
    model = BookingLog
    fields = ['booking','old_status','new_status']
    template_name = 'hotel_web/bookinglog_form.html'
    success_url = reverse_lazy('hotel_web:bookinglog_list')

class BookingLogDeleteView(DeleteView):
    model = BookingLog
    template_name = 'hotel_web/bookinglog_confirm_delete.html'
    success_url = reverse_lazy('hotel_web:bookinglog_list')

def customers_table(request):
    customers = Customer.objects.using('colleague').all()
    return render(request, "hotel_web/colleague_templates/customers_table.html", {"customers": customers})

@csrf_exempt
def delete_customer(request, customer_id):

    if request.method == "POST":
        customer = get_object_or_404(Customer.objects.using('colleague'), pk=customer_id)
        customer.delete(using='colleague')
    return redirect('hotel_web:customers-table')

