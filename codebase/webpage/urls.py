from django.urls import path, include
from . import views

from .views import (
    HomePageView,
    UpdateBinanceSymbolView,
    WalletView,
    UpdateWalletAssetView,
    UpdateCryptoBotSettingsView,
    ManageCoinAddView,
    ManageCoinDelView,
    CryptoDetailView,
    autocompleteAdd,
    autocompleteDel,
    SearchResults,
    GetOldOhlcvView,
    StartWebSocketView
)




urlpatterns = [
    path("", HomePageView.as_view(), name="homepage"),
    path("wallet.html", WalletView.as_view(), name="WalletView"),
    path("manage-coin.html", ManageCoinAddView.as_view(), name="ManageCoinAddView"),
    path("manage-coin.html/update-binance-list/", UpdateBinanceSymbolView.as_view(), name="UpdateBinanceSymbol"),
    path("manage-coin.html/delete-coin/", ManageCoinDelView.as_view(), name="ManageCoinDelView"),
    path("Wallet/Update_Asset/", UpdateWalletAssetView.as_view(), name="UpdateWalletAsset"),
    path("settings.html", UpdateCryptoBotSettingsView.as_view(), name="UpdateCryptoBotSettings"),
    path('autocompleteAdd', views.autocompleteAdd, name='autocompleteAdd'),
    path('autocompleteDel', views.autocompleteDel, name='autocompleteDel'),
    path("dashboard/<slug:slug>/", CryptoDetailView.as_view(), name="CryptoDetails"),
    path("search/<str:search>/", views.SearchResults, name= "SearchResults"),
    path("dashboard/<str:asset>/get-old-ohlcv/", GetOldOhlcvView.as_view(), name="GetOldOhlcv"),
    path("dashboard/<str:asset>/start-websocket/", StartWebSocketView.as_view(), name="StartWebSocket")
    # path("dashboard/<str:asset>/start-websocket/", views.StartWebSocketView, name="StartWebSocket")
]
