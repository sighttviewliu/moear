from django.test import TestCase

import logging

from .serializers import *


log = logging.getLogger(__name__)


class PostSerializerTests(TestCase):
    def test_create_with_fake_data(self):
        """
        根据假定数据进行序列化处理，并验证结果是否符合预期
        """
        fake_data_spider = {
            "name": "post_test",
            "display_name": "Post测试",
            "author": "小貘",
            "email": "xx@xxxx.com",
        }
        fake_data_post = {
            "spider": "post_test",
            "origin_url": "for-post-test",
            "title": "《红海行动》和《战狼 2》相比，突出了我们是人不是神",
            "content": "<div class=\"main-wrap content-wrap\">\n<div class=\"headline\">\n<div class=\"img-place-holder\"></div>\n</div>\n<div class=\"content-inner\">\n<div class=\"question\">\n<h2 class=\"question-title\">如何评价电影《红海行动》？</h2>\n<div class=\"answer\">\n<div class=\"meta\">\n<img class=\"avatar\" src=\"http://pic2.zhimg.com/v2-3ee29b89dbb5ba115c5ed068e4313ea1_is.jpg\"/>\n<span class=\"author\">深海，</span><span class=\"bio\">曾中国人民解放军陆军特种部队成员</span>\n</div>\n<div class=\"content\">\n<p>春节忙于走亲串友，昨晚抽时间去看了一个夜场。</p>\n<p>很多人说这个片子比战狼好看。我感觉各有特色吧，战狼突出了中国在世界上的地位，红海突出了团队协作，而且打破了主角光环不死的神话，石头和通讯员牺牲那一段看得我几乎泪目。战狼里面三人完好无损是没有可比性的。我们都是人，不是神。</p>\n<p>几个槽点，</p>\n<p>第一个，海上那段，海盗跑了绝对不会冒险去捉活的，没人会这么蠢，尤其是对方来了好几只船接应的时候，一枪打死不就完了吗，直升机舱门大开，对方几只冲锋枪集火射击就够你喝一壶的。</p>\n<p>第二个，小队乘坐悍马车通过交火区的时候，一群人就那么在敞篷悍马上正襟危坐，呼呼隆隆过去，任子弹在不足一百米的地方飞来飞去。</p>\n<p>第三个，海清，海清的演技无可厚非，在沙漠里被袭击以后，为了服从命令的问题和张译争论。万一你命令下错了呢？张译还好声好气的劝，真到了那种时候，要不就让她自己想去哪去哪，要不就直接绑起来带走，别问我为什么，这样的人是个定时炸弹，太过于自我，这样的人不光会害死自己，还会拉一群人当垫背的。</p>\n<p>第四个，那个扛机枪的女汉子，角色安排的不错，演技也不错，她用的枪我不知道是什么型号，因为我没用过，但是，挂弹链的机枪，我使用过的国内的，枪身最起码近 30 斤，加上弹鼓，50 斤有了，抵肩瞄准举着打？？我反正是扛不动的。还有最后近身格斗锁喉勒死那个大胡子的时候，真是力气惊人。琢磨一下，扛重机枪打也就可以理解了。</p>\n<p>评论区一些说这叫裸跤，不好意思我告诉你们，在部队格斗里面，这叫锁喉。别跟我整些有的没的，更不要秀所谓的:你居然连裸跤都不认识。我没兴趣知道起源哪里，在你眼里叫什么名字，更不需要你在我这里秀名词儿。格斗的时候我会使就行了。</p>\n<p>(更正一下，我一开始以为女汉子用的是重机枪，因为本人使用过的国内的加弹链的机枪最起码都在 30 斤以上，</p>\n<p>经评论区一些人提醒后翻阅相关资料，片中为 M249 机枪，整体重量在 12 公斤左右。但是就算是 12 公斤，像片中那样使用也是极度不现实的。</p>\n<p>抵肩射击需要极大的臂力和稳定性。一个 10 多公斤的枪支一直端着打，而且后座力带来的冲击是持续的，对一个男性特种兵来说也不实际。</p>\n<p>本人以前经常使用的是 95 式步枪，战斗全重估计在 5.6 公斤左右？具体没称过。在做完各种战术动作，奔袭，跑步以后的大体力消耗以后，抵肩射击都持续不了一个弹夹的时间。更不要提一个女兵在战场环境下使用十几公斤的枪支持续进行抵肩射击，评论区一群键盘侠说不重，我建议你们去跑个负重 5 公里，然后做 100 个俯卧撑，再举着个十斤重的铁家伙在你肩膀处不停抖动，持续 3 分钟算我输，我真心搞不懂你们这帮人是真不懂还是天生神力，光会一张嘴逼逼跟我整数据，不好意思我当兵的时候就不怎么学这些数据，你问任何一个基层作战部队军人详细数据，能回答出来的一百个也没有一个。我天天吃饭我还需要知道每个食物的卡路里和热量吗？不需要。因为我压根用不到。)</p>\n<p>第五个，蝙蝠衣，好几个人问我这个东西，我只能说，我没见过。我会飞三角翼，也会跳伞，但是我真的没见过我军会飞翼装。</p>\n<p>回答几个私信问题，第一个，海清端起枪就能用的问题，我个人觉得，她常年在这种环境下，肯定也对枪支射击有了解，最普通的 AK 端起来就能打也正常，不过，不会战术动作保护自己，盲目射击导致一轮扫射以后被打断手脚，也是情理之中。</p>\n<p>第二，特战会不会开坦克的问题，一部分参加过集训人会。国产坦克我会开 59，79，96，86 步战车也能玩，三角翼也飞过，大部分的汽车都会开，能开起来跑，但是不精通。几个人开坦克的时候，各种操作玩的那么溜，有点夸张了。一专多能是特种兵的必备技能。悍马没开过，上图证明。</p>\n<p>这是三角翼。</p>\n<p><img alt=\"\" class=\"content-image\" src=\"http://pic1.zhimg.com/70/v2-b0ab1aa051e60ad2780f6cab717c6310_b.jpg\"/></p>\n<p>枪支的问题，外军枪支学过，因为很多联合训练，都会学习外军枪支使用，我们单位也有一部分供学习参考。这个不足为奇。</p>\n<p>其他的不做多说了，毕竟如果较真的话就没意思了。我朋友说这电影特别棒，强烈推荐我看，我说，你觉得特别棒，可能我不会，因为很多时候，行内的人，会用不同于普通观众的角度来看一部电影。就类似于医生看医护电视剧那样。单纯看热闹和看门道差距太大了。</p>\n<p>下面是几个我觉得特别棒的地方。</p>\n<p>第一个就是炸弹爆炸的威力和迫击炮，几个人在路边正说话，咻的一声，那个尖利的炮弹破空声音听得我头皮发麻。看口径应该是 82 毫米的迫击炮，那个威力真的特别写实，除了没有破片伤人，迫击炮的位置，距离，发射形态，大巴上的人被炸的血肉模糊的样子，都几乎完美了。</p>\n<p>我军战士受伤以后，掏出来的急救针，那个针在我作训服左上衣口袋里装了好多年。三支，强心针，血清，防毒，三种颜色，几毫米的针头，按压大腿自主注射。这都是救命的东西。</p>\n<p>战场心理素质这是这部电影最大的亮点，太多太多的电影把主角塑造成了不知疲惫，没有感情，不畏生死的超人战士，但是在红海行动中，我看到了我们的战士防弹衣里面的照片，观察手面对子弹时候的惧怕，一群人在躲着的时候，特战队员满脸的汗，急促的呼吸声，眼神里面透露出来的不安的情感，近身格斗厮杀那段，用牙咬，用头撞，用尽所有手段去杀死对方，通讯员断掉的手指，石头被炸烂的左脸，还有靠近窗户被手雷炸掉的胳膊，那才是战争真实写照，这才是血肉铸造的人。</p>\n<p>下图是模拟战场环境下的集训截图，在不停的枪炮声和呼喊，爆炸干扰下，每一个攀登，甚至奔跑动作都会不自觉的变形，失去身体控制，大部分人的本能反应会超越你平时所学的所有训练动作，只有通过长时间的模拟环境训练才能达到在那种极端条件下保持冷静和正常思考。</p>\n<p><img alt=\"\" class=\"content-image\" src=\"http://pic3.zhimg.com/70/v2-593680e78abdd5363ac0da9b7d805b92_b.jpg\"/></p>\n<p>轰鸣的枪炮声，令人作呕的血腥味，映入眼帘的断指残躯，不间断的哀嚎和呻吟。随处可见的尸体，你不知道哪里会飞来一颗子弹掀掉你的头盖骨，也不知道你藏身的地方会不会被呼啸而来的炮弹炸成碎末，把你永远的掩埋在里面，你死去很久，腐烂发臭了，衣物腐朽，尸骨无存，外面的战火还没有熄灭。</p>\n<p>你就像任何一个你在电视新闻里面看到的炸弹袭击死去的数字一样。十几人，二十几人，一百多人，你只是其中一个。没人会知道你是谁。</p>\n<p>张译说，我们只营救那个中国人。其他人，对不起，没有时间。</p>\n<p>这才是现实，因为你在国内，你被保护得很好，所以你才不知道你有多幸福。</p>\n<p>西北边境，西南边境，每年都有死伤的战士，我曾在边境巡逻了一个月，每天出去都是几十人全副武装。前几年我上过海军潍坊舰和一个战友吃过饭，他们刚护航回来。最后的那两块姓名牌。不是虚构的，多少的烈士，烈属，你不知道并不代表他们不存在。你觉得世界很安全，是因为一直有人把枪炮声挡在了你看不到的地方。炸伤的战士说，好疼啊。通讯员看到自己的断指之后发出的哀嚎，石头炸残的脸露出的森森白牙和渐渐消失的呼吸。这些都让我难过得几乎落泪。</p>\n<p>活着不好吗？我觉得挺好的。</p>\n<p>最后，致敬每一个在我们看不到的地方守护共和国的军人。我为曾是其中一员而终身骄傲。</p>\n<p>敬礼。</p>\n</div>\n</div>\n<div class=\"answer\">\n<div class=\"meta\">\n<img class=\"avatar\" src=\"http://pic4.zhimg.com/f6e94cbe12f77a5cf5be0ed45f48a6db_is.jpg\"/>\n<span class=\"author\">李小懂</span>\n</div>\n<div class=\"content\">\n<p>大年初一，带着爸妈和弟弟，在十八线小县城，看《红海行动》。</p>\n<p>这部片排片率不是很高，我们本来是想买下午 2 点那场的，没票了，所以买了 5 点的，去看的时候厅内爆满，各种年龄段的人都有。</p>\n<p>我不太懂装备型号，也不太懂部队编制，所以我只能从一个非军事迷的女性观众的视角说一下这部电影的观感。</p>\n<p>1.战争场面真实残酷，爆炸、枪战、肉搏，满眼血肉横飞，全程精神紧绷，却不会引起极度不适。</p>\n<p>我是一个看到血腥场面生理上会有极度不适的人，大学舍友追《行尸走肉》和《吸血鬼》的时候我就因为里面一些略带血淋淋的场景一直没法一起追，看了一部《沉默的羔羊》，心理阴影到现在。</p>\n<p>《红海行动》虽然有许多细致描写断肢和血肉的镜头，但却并没有让我感到恶心和反胃，上一部没有让我觉得反胃的是《血战钢锯岭》。</p>\n<p>被迫击炮击中的巴士，由人类的躯体堆叠成的一片狼藉，伴随着遇难者的哀嚎，我没有觉得血腥的恶心，只是觉得如此人间惨象让人震撼，这是灾难。</p>\n<p>被汽车炸弹袭击的当地政府军，烧焦的尸体横陈街头，被炸的断腿还在颤抖，受伤者绝望的等待救援，枪炮声并没有因为这次惨烈的伤亡而停止，这是战争。</p>\n<p>被极端组织俘虏的威廉，从开头气定神闲与军方讨价还价，到被俘后虚弱的躺在病床上，还要面对对方头目非人类的虐待（这段我闭上眼没敢看），这是恐怖。</p>\n<p>影片没有用过多凄厉的惨叫来烘托惨烈的现场，更多的是低声甚至无声的镜头描写，却让我们真切感受到，我们因炸弹爆炸暂时失聪所以听不见哀嚎，以无声胜有声，你却能感到凄厉的战场。</p>\n<p>2.故事简洁不拖沓，台词基本没废话，没有多余的不必要情节，把观众当成智商正常的人。</p>\n<p>电影没有政治分明的纯正义与纯邪恶，没有无敌嘴遁，没有煽情回忆杀，没有非得把前因后果解释清楚的旁白，没有尴尬的感情线，没有因为忘带自家祖传信物必须回去拿而置主角于危险境地的侨民，没有哭喊着找妈妈死活不逃生的熊孩子，没有猪队友，没有立志要拯救全人类的大英雄。有的只是任务，只是保护中国人不受侵害的决心。一路看下来特别舒畅，没有让人上火的情节，没有傻的不会抉择的队员，我很欣慰。</p>\n<p>3.这也是作为一名女性观众感受最深认为最重要的一点，我感受到了这部片子里的男女平等。</p>\n<p>影片没有让女队员佟莉在战斗过程中无意间露出让人血脉喷张的曼妙身材，她全程裹得严严实实，头发还剃了板寸，拿起枪来英姿飒爽，开起车来风驰电掣。</p>\n<p>影片也没有让夏楠在与各路人马的交流中露出阴柔的易激发男人们保护欲的表情，她全程带着一副不怕死的冲劲儿，救人、开枪、被埋进沙里，与其他人无二致，没有享受所谓的“女性特权”。</p>\n<p>甚至是人质邓梅，在战争没发生之前，与丈夫和使馆人员的通话中，她也是不徐不疾稳住对方情绪，表示自己稍后会和公司的人一同离开。在战俘营中面对夏楠提出与她交换，她也没有含着眼泪说一些不可以我不能走你也是一条人命我做不到之类的话。</p>\n<p>全片弱化了演员们的女性特征，她们与男演员们同样坚毅勇敢机智决断，她们没有像别的影视作品一样把战友置于本不必要存在的危险境地，也没有愚蠢无脑延误战机，甚至在许多生死攸关的瞬间，她们起到了至关重要的作用。这作用不再是以往的感化和激励男主角，而是通过她们自己，将局面改变从而化险为夷。</p>\n<p>我感到一种尊重。</p>\n<p>许多影视作品中女性的存在只是点缀，只是为了调剂一下被战争场面迅速激生起的荷尔蒙。</p>\n<p>这部电影不一样，女性同样是战士，是团队的不可缺少的组成部分。只有在面对战友牺牲时，在得知助手的死讯时，才能看见她们展现出来的女性特质，才会意识到她们也是女的。</p>\n<p>然后，哭过发泄过之后，擦干眼泪，她们继续战斗。</p>\n<p>我觉得这酷毙了。</p>\n<p>中国的国际影响力与日俱增，在其他国家影视作品中不再是耍耍流氓搞搞小聪明这些投机的形象，更多的是无法撼动又值得托付和信任的大国形象。</p>\n<p>我希望在以后的影视作品中，也能更多的看到像《红海行动》这样，女性角色不再是调剂情节的点缀，而是作为不可缺少的一员，正向推进整个故事发展的影视作品。</p>\n<p>期待。</p>\n</div>\n</div>\n<div class=\"view-more\"><a href=\"http://www.zhihu.com/question/57848662\">查看知乎讨论<span class=\"js-question-holder\"></span></a></div>\n</div>\n</div>\n</div>",
            "date": "2018-02-22 00:00:00",
            "meta": [{
                "name": "spider.zhihu_daily.id",
                "value": 9670933
            }, {
                "name": "spider.zhihu_daily.top",
                "value": 1
            }, {
                "name": "moear.cover_image_slug",
                "value": "https://pic2.zhimg.com/v2-42bc560718c89adc1aa77e0c0a44af01.jpg"
            }]
        }

        spider, created = Spider.objects.get_or_create(
            name=fake_data_spider['name'],
            defaults=fake_data_spider)
        log.debug('获取Spider: {}， 创建: {}'.format(spider, created))
        post_serializer = PostSerializer(data=fake_data_post)
        if not post_serializer.is_valid():
            log.error(post_serializer.errors)
        self.assertIs(post_serializer.is_valid(), True)
        post_serializer.save()
        log.debug(post_serializer.instance)
        self.assertEqual(
            Post.objects.get(
                origin_url=fake_data_post['origin_url']),
            post_serializer.instance)
