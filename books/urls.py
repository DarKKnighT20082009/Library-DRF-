from django.urls import path

# from .views import BookListView, BookCreateView, BookDetailView, BookUpdateView, BookDeleteView, AuthorCreateView, \
#     AuthorDetailView, AuthorUpdateView, AuthorListView, AuthorDeleteView

from .views import BookListCreateView, BookRetrieveUpdateDestroyView

urlpatterns = [
    # path('', BookListView.as_view()),
    # path('create/', BookCreateView.as_view()),
    # path('<int:pk>/', BookDetailView.as_view()),
    # path('update/<int:pk>/', BookUpdateView.as_view()),
    # path('delete/<int:pk>/', BookDeleteView.as_view()),
    #
    # path('author/', AuthorListView.as_view()),
    # path('author_create/', AuthorCreateView.as_view()),
    # path('author/<int:pk>/', AuthorDetailView.as_view()),
    # path('author_update/<int:pk>/', AuthorUpdateView.as_view()),
    # path('author_delete/<int:pk>/', AuthorDeleteView.as_view()),

    path('bookscreate/', BookListCreateView.as_view()),
    path('booksingle/<int:pk>/', BookRetrieveUpdateDestroyView.as_view()),

]

