markets_names = ['Auchan', 'Carrefour', 'Kaufland', 'Penny', 'Profi', 'Mega Image']
markets_pictures = [
    'https://www.hellopark.ro/pictures/original/318255e7cfa2c1093c-auchan.jpg',
    'https://logowik.com/content/uploads/images/210_carrefour.jpg',
    'https://kaufland.media.schwarz/is/image/schwarz/t-kaufland-magazin%20%282%29?JGstbGVnYWN5LW9uc2l0ZS00JA==',
    'https://assets-eu-01.kc-usercontent.com/b50b8cce-450a-0138-7b43-de6bc2f3ad32/dfa9eff8-af7e-4d76-941f-226973049f2c/otopeni.jpg?w=1500&fm=webp&lossless=0&q=80',
    'https://storage0.dms.mpinteractiv.ro/media/1/1481/21335/22104753/1/profi.jpg',
    'https://www.shtiu.ro/wp-content/uploads/2018/09/mega-scaled.jpg',
]

blacklist = [
    'g', 'de', 'din', '+/-', 'la', 'un', 'kg', 'G', '%', 'cu', ',', 'l', 'punga', 'to',
    'auchan', 'cuburi', 'ready', 'eat', 'fresh', 'pe', 'bucata', 'pret', 'bucati',
    'netratate', 'dupa', 'recoltare', 'dupa', 'si', 'eco', 'red', 'delicious', 'golden',
    'idared', 'jonaprince', 'caserola', 'plasa', 'agriro', 'drink', 'grasime', 'ml', 'gr',
    'vrac', 'buc', 'pls', 'ptr', 'fiert', 'nrg', 'x', 'dz', 'pet', 'trk', 't', 'mg',
    'doza', 'nrgb', 'per',
]

supermarket_categories = [
    'legume', 'carne', 'mezeluri', 'lactate', 'bauturiNonAlcoolice', 'bauturiAlcoolice'
]

supermarket_category_labels = [
    'Fructe si legume', 'Carne si peste', 'Mezeluri', 'Lactate, branzeturi si oua',
    'Bauturi non-alcoolice', 'Bauturi alcoolice'
]

supermarket_category_icons = [
    'apple-svgrepo-com.svg', 'chicken-svgrepo-com.svg', 'sausage-svgrepo-com.svg',
    'cake-svgrepo-com.svg', 'water-cup-svgrepo-com.svg', 'beer-svgrepo-com.svg'
]

all_supermarkets = {
    'Auchan': {
        'legume': 'https://tazz.ro/timisoara/auchan-supermarket-timisoara/legume-si-fructe/12481/2597257/dpt',
        'carne': 'https://tazz.ro/timisoara/auchan-supermarket-timisoara/macelarie-si-peste/12481/2597278/dpt',
        'mezeluri': 'https://tazz.ro/timisoara/auchan-supermarket-timisoara/mezeluri-si-specialitati/12481/2597415/dpt',
        'lactate': 'https://tazz.ro/timisoara/auchan-supermarket-timisoara/lactate-branzeturi-si-oua/12481/2597300/dpt',
        'bauturiNonAlcoolice': 'https://tazz.ro/timisoara/auchan-supermarket-timisoara/bauturi-non-alcoolice/12481/2597489/dpt',
        'bauturiAlcoolice': 'https://tazz.ro/timisoara/auchan-supermarket-timisoara/bauturi-alcoolice/12481/2597564/dpt'
    },
    'Carrefour': {
        'legume': 'https://tazz.ro/timisoara/carrefour-timisoara-9113-/fructe-si-legume/21098/2249517/dpt',
        'carne': 'https://tazz.ro/timisoara/carrefour-timisoara-9113-/macelarie-si-peste/21098/2249519/dpt',
        'mezeluri': 'https://tazz.ro/timisoara/carrefour-timisoara-9113-/mezeluri/21098/2249520/dpt',
        'lactate': 'https://tazz.ro/timisoara/carrefour-timisoara-9113-/lactate-branzeturi-si-oua/21098/2249518/dpt',
        'bauturiNonAlcoolice': 'https://tazz.ro/timisoara/carrefour-timisoara-9113-/bauturi-nealcoolice/21098/2248355/dpt',
        'bauturiAlcoolice': 'https://tazz.ro/timisoara/carrefour-timisoara-9113-/bauturi-alcoolice/21098/2248357/dpt'
    },
    'Kaufland': {
        'legume': 'https://tazz.ro/timisoara/kaufland-timisoara/legume-si-fructe/3865/1800340/dpt',
        'carne': 'https://tazz.ro/timisoara/kaufland-timisoara/macelarie-si-peste/3865/1800367/dpt',
        'mezeluri': 'https://tazz.ro/timisoara/kaufland-timisoara/mezeluri-si-specialitati/3865/1800414/dpt',
        'lactate': 'https://tazz.ro/timisoara/kaufland-timisoara/lactate-branzeturi-si-oua/3865/1800380/dpt',
        'bauturiNonAlcoolice': 'https://tazz.ro/timisoara/kaufland-timisoara/bauturi-non-alcoolice/3865/1800425/dpt',
        'bauturiAlcoolice': 'https://tazz.ro/timisoara/kaufland-timisoara/bauturi-alcoolice/3865/1800448/dpt'
    },
    'Penny': {
        'legume': 'https://tazz.ro/timisoara/penny/legume-si-fructe/14719/2704623/dpt',
        'carne': 'https://tazz.ro/timisoara/penny/macelarie-si-peste/14719/2704633/dpt',
        'mezeluri': 'https://tazz.ro/timisoara/penny/mezeluri-si-specialitati/14719/2704632/dpt',
        'lactate': 'https://tazz.ro/timisoara/penny/lactate-branzeturi-si-oua/14719/2704631/dpt',
        'bauturiNonAlcoolice': 'https://tazz.ro/timisoara/penny/bauturi-non-alcoolice/14719/2704624/dpt',
        'bauturiAlcoolice': 'https://tazz.ro/timisoara/penny/bauturi-alcoolice/14719/2704622/dpt'
    },
    'Profi': {
        'legume': 'https://tazz.ro/timisoara/profi/fructe-si-legume/19674/1776919/dpt',
        'carne': 'https://tazz.ro/timisoara/profi/carne/19674/1776929/cat',
        'mezeluri': 'https://tazz.ro/timisoara/profi/mezeluri/19674/1776980/dpt',
        'lactate': 'https://tazz.ro/timisoara/profi/lactate-si-oua/19674/1776952/dpt',
        'bauturiNonAlcoolice': 'https://tazz.ro/timisoara/profi/bauturi-non-alcoolice/19674/1776997/dpt',
        'bauturiAlcoolice': 'https://tazz.ro/timisoara/profi/bauturi-alcoolice/19674/1777011/dpt'
    },
    'Mega Image': {
        'legume': 'https://tazz.ro/timisoara/mega-image-timisoara/legume-si-fructe/1535/1789150/dpt',
        'carne': 'https://tazz.ro/timisoara/mega-image-timisoara/macelarie-si-peste/1535/1789215/dpt',
        'mezeluri': 'https://tazz.ro/timisoara/mega-image-timisoara/mezeluri-si-specialitati/1535/1789350/dpt',
        'lactate': 'https://tazz.ro/timisoara/mega-image-timisoara/lactate-branzeturi-si-oua/1535/1789247/dpt',
        'bauturiNonAlcoolice': 'https://tazz.ro/timisoara/mega-image-timisoara/bauturi-non-alcoolice/1535/1789372/dpt',
        'bauturiAlcoolice': 'https://tazz.ro/timisoara/mega-image-timisoara/bauturi-alcoolice/1535/1789436/dpt'
    }
}
