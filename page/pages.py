# -*- coding: utf-8 -*-
from page import tools

pages = tools.parse()


def get_locater(clazz_name, method_name):
    locators = pages[clazz_name]['locators']
    for locator in locators:
        if locator['name'] == method_name:
            return locator


class LoginPage:

    fb = get_locater('LoginPage', 'fb')
    google = get_locater('LoginPage', 'google')
    google_choose = get_locater('LoginPage', 'google_choose')
    twitter = get_locater('LoginPage', 'twitter')
    twitter_choose = get_locater('LoginPage', 'twitter_choose')
    login_later = get_locater('LoginPage', 'login_later')
    login_mail = get_locater('LoginPage', 'login_mail')
    login_password = get_locater('LoginPage', 'login_password')
    login_button = get_locater('LoginPage', 'login_button')


class MainPage:
    discover_album_name = get_locater('MainPage', 'discover_album_name')
    search = get_locater('MainPage', 'search')
    genres = get_locater('MainPage', 'genres')
    genres_list = get_locater('MainPage', 'genres_list')
    genres_list_album_name = get_locater('MainPage', 'genres_list_album_name')
    my_library = get_locater('MainPage', 'my_library')
    recents = get_locater('MainPage', 'recents')
    download = get_locater('MainPage', 'download')
    nav_drawer = get_locater('MainPage', 'nav_drawer')
    login = get_locater('MainPage', 'login')
    close = get_locater('MainPage', 'close')
    close_offer = get_locater('MainPage', 'close_offer')
    select_all = get_locater('MainPage', 'select_all')
    continue_bn = get_locater('MainPage', 'continue_bn')


class ProfilePage:
    user_name = get_locater('ProfilePage', 'user_name')


class AlbumDetailsPage:
    album_name = get_locater('AlbumDetailsPage', 'album_name')
    chapter_name = get_locater('AlbumDetailsPage', 'chapter_name')
    popular_user_name = get_locater('AlbumDetailsPage', 'popular_user_name')
    popular_user_view = get_locater('AlbumDetailsPage', 'popular_user_view')


class RecordPage:
    record = get_locater('RecordPage', 'record')
    upload = get_locater('RecordPage', 'upload')
    play = get_locater('RecordPage', 'play')
    time = get_locater('RecordPage', 'time')
    title = get_locater('RecordPage', 'title')


class UploadPage:
    save = get_locater('UploadPage', 'save')
    post = get_locater('UploadPage', 'post')
    upload = get_locater('UploadPage', 'upload')
    play = get_locater('UploadPage', 'play')
    time = get_locater('UploadPage', 'time')
    select_album = get_locater('UploadPage', 'select_album')
    text_episode = get_locater('UploadPage', 'text_episode')
    text_view = get_locater('UploadPage', 'text_view')
    create_album = get_locater('UploadPage', 'create_album')
    later = get_locater('UploadPage','later')
    album_name = get_locater('UploadPage','Dancer')


class MystdioPage:
    album_name = get_locater('MystdioPage', 'album_name')
    create_album = get_locater('MystdioPage', 'create_album')
    Draft = get_locater('MystdioPage', 'Draft')
    create_album_add = get_locater('MystdioPage', 'create_album_add')
    edit = get_locater('MystdioPage', 'edit')
    delete = get_locater('MystdioPage', 'delete')
    delete_ok = get_locater('MystdioPage', 'delete_ok')
    sort = get_locater('MystdioPage', 'sort')


class CreateAlbumPage:
    create_album_cover = get_locater('CreateAlbumPage', 'create_album_cover')
    create_album_title = get_locater('CreateAlbumPage', 'create_album_title')
    create_author = get_locater('CreateAlbumPage', 'create_author')

    create_description = get_locater('CreateAlbumPage', 'create_description')
    create_album_add = get_locater('CreateAlbumPage', 'create_album_add')
    take_photo = get_locater('CreateAlbumPage', 'take_photo')
    choose_from_album = get_locater('CreateAlbumPage', 'choose_from_album')
    picture = get_locater('CreateAlbumPage', 'picture')
    menu_crop = get_locater('CreateAlbumPage', 'menu_crop')
    genre = get_locater('CreateAlbumPage', 'genre')
    genre_choose = get_locater('CreateAlbumPage', 'genre_choose')


class ToolPage:
    user_name = get_locater('ToolPage', 'user_name')
    title = get_locater('ToolPage', 'title')
    login_btn = get_locater('ToolPage', 'login_btn')
    record = get_locater('ToolPage', 'record')
    studio = get_locater('ToolPage', 'studio')


class EpisodePlayPage:
    album_name = get_locater('EpisodePlayPage', 'album_name')
    chapter_name = get_locater('EpisodePlayPage', 'chapter_name')
    play_time = get_locater('EpisodePlayPage', 'play_time')
    total_time = get_locater('EpisodePlayPage', 'total_time')
    action = get_locater('EpisodePlayPage', 'action')
    delete = get_locater('EpisodePlayPage', 'delete')
    delete_ok = get_locater('EpisodePlayPage', 'delete_ok')
    play_iv = get_locater('EpisodePlayPage', 'play_iv')
    play_next = get_locater('EpisodePlayPage', 'play_next')


class RecentsPage:
    episode_name = get_locater('RecentsPage', 'episode_name')
    album_name = get_locater('RecentsPage', 'album_name')