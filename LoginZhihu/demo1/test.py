#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
@file: demo1.test

@email: 412425870@qq.com

@author: Cay
'''
from bs4 import BeautifulSoup

s = '<div class="zm-profile-section-item zg-clear" id="tpi-68" data-tid="ftid-68"><div class="zm-profile-section-main"><a href="/topic/19550429" data-hovercard="t$t$19550429"><strong>电影</strong></a><div class="zm-editable-content"></div><div><a class="zg-link-gray" href="/people/mu-shi-qian-meng-49/topic/19550429/answers">0 个回答</a></div></div></div><div class="zm-profile-section-item zg-clear" id="tpi-1093" data-tid="ftid-1093"><a class="zm-list-avatar-link" href="/topic/19553510"><img class="zm-list-avatar-medium" src="https://pic2.zhimg.com/2e6276881_xs.jpg"></a><div class="zm-profile-section-main"><a data-follow="t:button" href="javascript:;" class="zg-right zg-btn zg-btn-unfollow" id="tp-1093">取消关注</a><a href="/topic/19553510" data-hovercard="t$t$19553510"><strong>算法</strong></a><div class="zm-editable-content"></div><div><a class="zg-link-gray" href="/people/mu-shi-qian-meng-49/topic/19553510/answers">0 个回答</a></div></div></div><div class="zm-profile-section-item zg-clear" id="tpi-7240" data-tid="ftid-7240"><a class="zm-list-avatar-link" href="/topic/19571906"><img class="zm-list-avatar-medium" src="https://pic2.zhimg.com/a4541c3d230a7e69b52c874ea52b9555_xs.jpg"></a><div class="zm-profile-section-main"><a data-follow="t:button" href="javascript:;" class="zg-right zg-btn zg-btn-unfollow" id="tp-7240">取消关注</a><a href="/topic/19571906" data-hovercard="t$t$19571906"><strong>旅行攻略</strong></a><div class="zm-editable-content"></div><div><a class="zg-link-gray" href="/people/mu-shi-qian-meng-49/topic/19571906/answers">0 个回答</a></div></div></div><div class="zm-profile-section-item zg-clear" id="tpi-75" data-tid="ftid-75"><a class="zm-list-avatar-link" href="/topic/19550453"><img class="zm-list-avatar-medium" src="https://pic4.zhimg.com/6b84ba24b698381d87d831cb01b201bb_xs.png"></a><div class="zm-profile-section-main"><a data-follow="t:button" href="javascript:;" class="zg-right zg-btn zg-btn-unfollow" id="tp-75">取消关注</a><a href="/topic/19550453" data-hovercard="t$t$19550453"><strong>音乐</strong></a><div class="zm-editable-content"></div><div><a class="zg-link-gray" href="/people/mu-shi-qian-meng-49/topic/19550453/answers">0 个回答</a></div></div></div><div class="zm-profile-section-item zg-clear" id="tpi-81491" data-tid="ftid-81491"><a class="zm-list-avatar-link" href="/topic/19793302"><img class="zm-list-avatar-medium" src="https://pic3.zhimg.com/72c987596_xs.jpg"></a><div class="zm-profile-section-main"><a data-follow="t:button" href="javascript:;" class="zg-right zg-btn zg-btn-unfollow" id="tp-81491">取消关注</a><a href="/topic/19793302" data-hovercard="t$t$19793302"><strong>MOOCs</strong></a><div class="zm-editable-content"></div><div><a class="zg-link-gray" href="/people/mu-shi-qian-meng-49/topic/19793302/answers">0 个回答</a></div></div></div><div class="zm-profile-section-item zg-clear" id="tpi-32352" data-tid="ftid-32352"><a class="zm-list-avatar-link" href="/topic/19647099"><img class="zm-list-avatar-medium" src="https://pic3.zhimg.com/853d7134586d8aa5585eeb6568074262_xs.png"></a><div class="zm-profile-section-main"><a data-follow="t:button" href="javascript:;" class="zg-right zg-btn zg-btn-unfollow" id="tp-32352">取消关注</a><a href="/topic/19647099" data-hovercard="t$t$19647099"><strong>旅行计划</strong></a><div class="zm-editable-content"></div><div><a class="zg-link-gray" href="/people/mu-shi-qian-meng-49/topic/19647099/answers">0 个回答</a></div></div></div><div class="zm-profile-section-item zg-clear" id="tpi-98" data-tid="ftid-98"><a class="zm-list-avatar-link" href="/topic/19550516"><img class="zm-list-avatar-medium" src="https://pic3.zhimg.com/891b4f32a_xs.jpg"></a><div class="zm-profile-section-main"><a data-follow="t:button" href="javascript:;" class="zg-right zg-btn zg-btn-unfollow" id="tp-98">取消关注</a><a href="/topic/19550516" data-hovercard="t$t$19550516"><strong>Web 开发</strong></a><div class="zm-editable-content"></div><div><a class="zg-link-gray" href="/people/mu-shi-qian-meng-49/topic/19550516/answers">0 个回答</a></div></div></div><div class="zm-profile-section-item zg-clear" id="tpi-99" data-tid="ftid-99"><a class="zm-list-avatar-link" href="/topic/19550517"><img class="zm-list-avatar-medium" src="https://pic4.zhimg.com/f07808da5625fef3607f8b75b770349f_xs.jpg"></a><div class="zm-profile-section-main"><a data-follow="t:button" href="javascript:;" class="zg-right zg-btn zg-btn-unfollow" id="tp-99">取消关注</a><a href="/topic/19550517" data-hovercard="t$t$19550517"><strong>互联网</strong></a><div class="zm-editable-content"></div><div><a class="zg-link-gray" href="/people/mu-shi-qian-meng-49/topic/19550517/answers">0 个回答</a></div></div></div><div class="zm-profile-section-item zg-clear" id="tpi-103" data-tid="ftid-103"><a class="zm-list-avatar-link" href="/topic/19550532"><img class="zm-list-avatar-medium" src="https://pic3.zhimg.com/dc28deb4e_xs.jpg"></a><div class="zm-profile-section-main"><a data-follow="t:button" href="javascript:;" class="zg-right zg-btn zg-btn-unfollow" id="tp-103">取消关注</a><a href="/topic/19550532" data-hovercard="t$t$19550532"><strong>YouTube</strong></a><div class="zm-editable-content"></div><div><a class="zg-link-gray" href="/people/mu-shi-qian-meng-49/topic/19550532/answers">0 个回答</a></div></div></div><div class="zm-profile-section-item zg-clear" id="tpi-618" data-tid="ftid-618"><a class="zm-list-avatar-link" href="/topic/19552067"><img class="zm-list-avatar-medium" src="https://pic3.zhimg.com/6e292ef66_xs.jpg"></a><div class="zm-profile-section-main"><a data-follow="t:button" href="javascript:;" class="zg-right zg-btn zg-btn-unfollow" id="tp-618">取消关注</a><a href="/topic/19552067" data-hovercard="t$t$19552067"><strong>数据库</strong></a><div class="zm-editable-content"></div><div><a class="zg-link-gray" href="/people/mu-shi-qian-meng-49/topic/19552067/answers">0 个回答</a></div></div></div><div class="zm-profile-section-item zg-clear" id="tpi-161387" data-tid="ftid-161387"><a class="zm-list-avatar-link" href="/topic/20027689"><img class="zm-list-avatar-medium" src="https://pic1.zhimg.com/e82bab09c_xs.jpg"></a><div class="zm-profile-section-main"><a data-follow="t:button" href="javascript:;" class="zg-right zg-btn zg-btn-unfollow" id="tp-161387">取消关注</a><a href="/topic/20027689" data-hovercard="t$t$20027689"><strong>Python教程</strong></a><div class="zm-editable-content"></div><div><a class="zg-link-gray" href="/people/mu-shi-qian-meng-49/topic/20027689/answers">0 个回答</a></div></div></div><div class="zm-profile-section-item zg-clear" id="tpi-108" data-tid="ftid-108"><a class="zm-list-avatar-link" href="/topic/19550547"><img class="zm-list-avatar-medium" src="https://pic3.zhimg.com/a5488c5ea_xs.jpg"></a><div class="zm-profile-section-main"><a data-follow="t:button" href="javascript:;" class="zg-right zg-btn zg-btn-unfollow" id="tp-108">取消关注</a><a href="/topic/19550547" data-hovercard="t$t$19550547"><strong>移动互联网</strong></a><div class="zm-editable-content"></div><div><a class="zg-link-gray" href="/people/mu-shi-qian-meng-49/topic/19550547/answers">0 个回答</a></div></div></div><div class="zm-profile-section-item zg-clear" id="tpi-5229" data-tid="ftid-5229"><a class="zm-list-avatar-link" href="/topic/19565864"><img class="zm-list-avatar-medium" src="https://pic3.zhimg.com/f20bb57ca_xs.jpg"></a><div class="zm-profile-section-main"><a data-follow="t:button" href="javascript:;" class="zg-right zg-btn zg-btn-unfollow" id="tp-5229">取消关注</a><a href="/topic/19565864" data-hovercard="t$t$19565864"><strong>CSDN</strong></a><div class="zm-editable-content"></div><div><a class="zg-link-gray" href="/people/mu-shi-qian-meng-49/topic/19565864/answers">0 个回答</a></div></div></div><div class="zm-profile-section-item zg-clear" id="tpi-622" data-tid="ftid-622"><a class="zm-list-avatar-link" href="/topic/19552079"><img class="zm-list-avatar-medium" src="https://pic2.zhimg.com/a7b1cfd75_xs.jpg"></a><div class="zm-profile-section-main"><a data-follow="t:button" href="javascript:;" class="zg-right zg-btn zg-btn-unfollow" id="tp-622">取消关注</a><a href="/topic/19552079" data-hovercard="t$t$19552079"><strong>面试</strong></a><div class="zm-editable-content"></div><div><a class="zg-link-gray" href="/people/mu-shi-qian-meng-49/topic/19552079/answers">0 个回答</a></div></div></div><div class="zm-profile-section-item zg-clear" id="tpi-112" data-tid="ftid-112"><a class="zm-list-avatar-link" href="/topic/19550560"><img class="zm-list-avatar-medium" src="https://pic4.zhimg.com/b75f995419ff775ff71fca685d7825af_xs.jpg"></a><div class="zm-profile-section-main"><a data-follow="t:button" href="javascript:;" class="zg-right zg-btn zg-btn-unfollow" id="tp-112">取消关注</a><a href="/topic/19550560" data-hovercard="t$t$19550560"><strong>创业</strong></a><div class="zm-editable-content"></div><div><a class="zg-link-gray" href="/people/mu-shi-qian-meng-49/topic/19550560/answers">0 个回答</a></div></div></div><div class="zm-profile-section-item zg-clear" id="tpi-113" data-tid="ftid-113"><a class="zm-list-avatar-link" href="/topic/19550564"><img class="zm-list-avatar-medium" src="https://pic1.zhimg.com/3f30afdfc_xs.jpg"></a><div class="zm-profile-section-main"><a data-follow="t:button" href="javascript:;" class="zg-right zg-btn zg-btn-unfollow" id="tp-113">取消关注</a><a href="/topic/19550564" data-hovercard="t$t$19550564"><strong>阅读</strong></a><div class="zm-editable-content"></div><div><a class="zg-link-gray" href="/people/mu-shi-qian-meng-49/topic/19550564/answers">0 个回答</a></div></div></div><div class="zm-profile-section-item zg-clear" id="tpi-14455" data-tid="ftid-14455"><a class="zm-list-avatar-link" href="/topic/19593616"><img class="zm-list-avatar-medium" src="https://pic1.zhimg.com/e82bab09c_xs.jpg"></a><div class="zm-profile-section-main"><a data-follow="t:button" href="javascript:;" class="zg-right zg-btn zg-btn-unfollow" id="tp-14455">取消关注</a><a href="/topic/19593616" data-hovercard="t$t$19593616"><strong>编程学习</strong></a><div class="zm-editable-content"></div><div><a class="zg-link-gray" href="/people/mu-shi-qian-meng-49/topic/19593616/answers">0 个回答</a></div></div></div><div class="zm-profile-section-item zg-clear" id="tpi-20092" data-tid="ftid-20092"><a class="zm-list-avatar-link" href="/topic/19610306"><img class="zm-list-avatar-medium" src="https://pic2.zhimg.com/09602eae5_xs.jpg"></a><div class="zm-profile-section-main"><a data-follow="t:button" href="javascript:;" class="zg-right zg-btn zg-btn-unfollow" id="tp-20092">取消关注</a><a href="/topic/19610306" data-hovercard="t$t$19610306"><strong>Linux 开发</strong></a><div class="zm-editable-content"></div><div><a class="zg-link-gray" href="/people/mu-shi-qian-meng-49/topic/19610306/answers">0 个回答</a></div></div></div><div class="zm-profile-section-item zg-clear" id="tpi-41599" data-tid="ftid-41599"><a class="zm-list-avatar-link" href="/topic/19674721"><img class="zm-list-avatar-medium" src="https://pic3.zhimg.com/4bd5298afac736b1251d7ef554f84e22_xs.png"></a><div class="zm-profile-section-main"><a data-follow="t:button" href="javascript:;" class="zg-right zg-btn zg-btn-unfollow" id="tp-41599">取消关注</a><a href="/topic/19674721" data-hovercard="t$t$19674721"><strong>裸辞</strong></a><div class="zm-editable-content"></div><div><a class="zg-link-gray" href="/people/mu-shi-qian-meng-49/topic/19674721/answers">0 个回答</a></div></div></div><div class="zm-profile-section-item zg-clear" id="tpi-6551" data-tid="ftid-6551"><a class="zm-list-avatar-link" href="/topic/19569848"><img class="zm-list-avatar-medium" src="https://pic4.zhimg.com/673f9383b_xs.jpg"></a><div class="zm-profile-section-main"><a data-follow="t:button" href="javascript:;" class="zg-right zg-btn zg-btn-unfollow" id="tp-6551">取消关注</a><a href="/topic/19569848" data-hovercard="t$t$19569848"><strong>生活常识</strong></a><div class="zm-editable-content"></div><div><a class="zg-link-gray" href="/people/mu-shi-qian-meng-49/topic/19569848/answers">0 个回答</a></div></div></div>'
soup = BeautifulSoup(s, 'html.parser')
topics_div = soup.find_all('div', attrs={'class':'zm-profile-section-item zg-clear'})
print(topics_div[0])

for topics_node in topics_div:
    print(type(topics_node))
    #print(str(topics_node))
    soup = BeautifulSoup(topics_node, 'html.parser')
    topics = soup.find_all('strong')
    print(topics[0].get_text())