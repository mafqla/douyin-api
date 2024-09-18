require('./env')
require('./a_bogus')


function get_a_bogus(p) {
    arguments = [
        0,
        1,
        14,
        p,
        "",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
    ]
    var r = window.guo._v;
    return (0, window.guo._u)(r[0], arguments, r[1], r[2], this)
}

// //测试
// p = "device_platform=webapp&aid=6383&channel=channel_pc_web&detail_list=1&source=6&main_billboard_count=5&update_version_code=170400&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1847&screen_height=1039&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=125.0.0.0&browser_online=true&engine_name=Blink&engine_version=125.0.0.0&os_name=Windows&os_version=10&cpu_core_num=8&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7373962654656054793&msToken=Ckd2fI-_nfVG35paalAjIPTWjEdqhno6y_Sjw07L4EoTjqgfQAJqAm3q-Xwtq_35sKwY58JvEhdnIv1sDDk4438fu6n7vMm__eCqRVdAg552FZdi062kyJNE77qCD3A%3D&msToken=Ckd2fI-_nfVG35paalAjIPTWjEdqhno6y_Sjw07L4EoTjqgfQAJqAm3q-Xwtq_35sKwY58JvEhdnIv1sDDk4438fu6n7vMm__eCqRVdAg552FZdi062kyJNE77qCD3A%3D",
// console.log(get_a_bogus(p))