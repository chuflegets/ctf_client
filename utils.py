domains = ['corona-virusus.com', 'coronavirus.meds.com', 'coronaviruscontain.com', 'coronaviruscontained.com',
           'coronavirusfeedback.com', 'coronavirusharm.com', 'coronavirushazard.com', 'coronavirusmessage.com',
           'coronavirustrouble.com', 'fightcovid.profitabit.club', 'mask.coronaprotective.store',
           'coronavirus-guidance.com', 'nycovid-19cases.com', 'covidnewsupdate.online', 'covidvoiceportal.com',
           'portal-covid-19.ml', 'portal-covid-19.ga', 'ayangarts.or.kr', 'covid-19donor.com', 'covid19grantor.com',
           'covid-19donator.com', 'curecoronavirus.life', 'coronavirusresonancecure.com', 'acureforcoronavirus.org']

fake_domains = ['1004.in', 'aabiokyagdw.com', '4go2com.net', 'admediadelivery.co.cc', '6000000.in',
                'adobesupport.perl.sh', '7cy.net', 'ahaninuiae.publicvm.com', 'aeryboem.info', 'areacodeszone.in',
                'agrebleice.com', 'ashampoo-15.com', 'all4corp.com', 'ashampoo-18.com', 'aryahoo.info',
                'ashampoo-19.com', 'atlantisc.net', 'aztecinternational.com.au', 'avygamer.co.uk', 'basicreader.co.cc',
                'bassearch.info', 'beerhouse.cz.cc', 'bftop.ru', 'bladenraedes.org', 'blindry.com', 'cadastro-real.com',
                'butehotel.com', 'consorzionavigli.it', 'c010x1.co.cc', 'cronenstr.co.cc', 'coca4ka.info',
                'deseprotikast.com', 'cocala.info', 'dfasdgkgt.cz.cc', 'comcaste.co.cc', 'dfgytcodgdw.com',
                'coo0lnet.net', 'down.playdns.info', 'cozemu7.co.cc', 'drummingmad.com', 'ealo.net',
                'fgsdfsdffg3.co.cc', 'el-pics.com', 'for-advanced-cfg2.com', 'ellsearch.info', 'free-big-data.com',
                'etdw.co.cc', 'freeinfoareacode.com', 'fiberlinez.com', 'frilled-dragon.com', 'gate33.info',
                'funkystuffhere.kickme.to', 'genoeco.com', 'fvrwqtvedjqthln.com', 'greatreload.in', 'fx010413.whyi.org',
                'hmmikr.com', 'goforbroke.reads.it', 'jjwextxf.com', 'greatreactor.co.cc', 'jx2dbtwg.com',
                'help.iptables.ws', 'kaxn.ru', 'here.get-2011-version-now.info', 'kinokol.net', 'hockeyminnie.co.cc',
                'lider33.tk', 'huekacugegujed.linkpc.net', 'linkbuzz76.eu', 'jdfhdsgs4.co.cc', 'll12.ru',
                'ldn5.spiderwww.co.cc', 'loyeje5.co.cc', 'mediatracking.co.cc', 'megems.net', 'memoristeak.co.cc',
                'modaction.ru', 'microsoftwindowssecurity181.com', 'nefemo2.co.cc', 'next-file-server.com',
                'nofotoraid.net', 'olddesingqutim.com', 'nonononunu.com', 'online-alert-policy62.co.cc', 'ozone777.com',
                'onlyonyx10.com', 'parti20.co.cc', 'oooabterast0.co.cc', 'perconel.com', 'performancecarcompany.com',
                'pinkiz.com', 'popgoestheweek.com', 'poonstart.ru', 'porn-hunt.cz.cc', 'qwwww.co.cc',
                'porn-hunter.cz.cc', 'redfjhsfk.com', 'porntubexxl.com', 'reketfoto.ru', 'postcardsservices.net',
                'rfushop.com', 'privateconfigurationforme.com', 'sercaag.com', 'searchalthough.org', 'sgtewkhk.biz',
                'serpentarium.cv.ua', 'spbing.com', 'snobchyct.info', 'tinki.jino.ru', 'steamcastlerun.co.cc',
                'trevorsee.net', 'supercybersecurity.com', 'usofrance.fr', 'systemdllsupd.ru', 'usosop.com',
                'time-sync-24.net', 'veicl.net', 'time-sync-24y.net', 'vkotalke.info', 'unnurhmint.com', 'w1zzz.com',
                'unubiglenr.com', 'webyeeworx.com', 'vandelivens.org', 'wedness.cv.ua', 'winhostmanager.net',
                'x1x4x0.net', 'winupdatecontrol.net', 'zedoze9.co.cc', 'zunder.facelookbs.net']

pieces = dict()


def spell(domain):
    return [ch for ch in domain]


if __name__ == '__main__':
    flag = 'g3t_t3st3d_f0r_d4_v1ru5'
    flag_spell = spell(flag)
    domain_spells = [spell(domain) for domain in fake_domains]
    #broken_virii = list(zip(flag_spell, domain_spells))
    #fixed_virii = [{'letter': broken_virus[0], 'pieces': broken_virus[1]} for broken_virus in broken_virii]

    print(domain_spells)