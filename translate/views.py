from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.shortcuts import render

import  sys
import boto3
from contextlib import closing


from .forms import French
from googletrans import Translator


def translateEnglishToFrench(text):
    translator = Translator()
    return translator.translate(text, src='en', dest='fr').text


class HomePageView(TemplateView):
    message = None
    template_name = "translate/index.html"


def home(request):

    if 'string' in request.POST:
        text = request.POST['string']
        message = translateEnglishToFrench(request.POST['string'])
    else:
        message = ''
        text = ''

    client = boto3.client('polly')
    response = client.synthesize_speech(
        OutputFormat='mp3',
        Text=message,
        TextType='text',
        VoiceId='Joanna'
    )
    print (response)
    if "AudioStream" in response:
        with closing(response["AudioStream"]) as stream:
            output = "translate/static/translate/polly-boto.mp3"

            try:
                # Open a file for writing the output as a binary stream
                with open(output, "wb") as file:
                    file.write(stream.read())
            except IOError as error:
                # Could not write to file, exit gracefully
                print(error)
                sys.exit(-1)

    return render(request, 'translate/index.html', {
        'message': message,
        'text': text,
        'audio': response,
    })

# def home(request):
#     path, _, query_string = self.path.partition('?')
#     query = parse_qs(query_string)
#
#     response = None
#
#     print(u"[START]: Received GET for %s with query: %s" % (path, query))
#
#     try:
#         # Handle the possible request paths
#         if path == ROUTE_INDEX:
#             response = self.route_index(path, query)
#         elif path == ROUTE_VOICES:
#             response = self.route_voices(path, query)
#         elif path == ROUTE_READ:
#             response = self.route_read(path, query)
#         else:
#             response = self.route_not_found(path, query)
#
#         self.send_headers(response.status, response.content_type)
#         self.stream_data(response.data_stream)
#
#     except HTTPStatusError as err:
#         # Respond with an error and log debug
#         # information
#         if sys.version_info >= (3, 0):
#             self.send_error(err.code, err.message, err.explain)
#         else:
#             self.send_error(err.code, err.message)
#
#         self.log_error(u"%s %s %s - [%d] %s", self.client_address[0],
#                        self.command, self.path, err.code, err.explain)
#
#     print("[END]")


# def search(request):
#     if 'string' in request.GET:
#         message = translateEnglishToFrench(request.GET['string'])
#     else:
#         message = 'You submitted an empty form.'
#     return HttpResponse(message)

