export const productData = {
  // 메인 정보 (과일 바꿀 때 여기서 한 번만 바꾸면 전체 페이지에 적용됩니다)
  fruitName: "참외",
  region: "성주",
  brix: 19,
  brandName: "푸드지",
  
  // 텍스트 커스터마이징
  heroSubtitle: "더이상 속지 마세요!",
  heroTitle: "저희 참외\n정말 맛있습니다!",
  heroWarning: "타업체 같은 품질 낮은\n떨이 참외가 아닙니다!",
  heroBrixHighlight: "압도적 당도 19brix",
  
  // 이미지 URL (언스플래시 임시 이미지 적용됨, 대표님 실제 사진으로 교체하세요)
  images: {
    hero: "https://images.unsplash.com/photo-1595493863486-8d69f3a6cb6e?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
    point1_1: "https://images.unsplash.com/photo-1595493863486-8d69f3a6cb6e?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
    point1_2: "https://images.unsplash.com/photo-1595493863486-8d69f3a6cb6e?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
    point2_1: "https://images.unsplash.com/photo-1595493863486-8d69f3a6cb6e?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
    point2_2: "https://images.unsplash.com/photo-1595493863486-8d69f3a6cb6e?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
  },
  
  // 비교 테이블 데이터
  competitor: {
    name: "타사 상품",
    points: ["국내산", "신선하지 않음", "선별 미확인", "낮은 당도 오이 맛"]
  },
  ourProduct: {
    name: "푸드지 성주 꿀 참외",
    points: ["참외의 고장 성주", "당일수확 당일발송", "전문가 당도 선별", "평균 19brix 고당도"]
  },

  // 당도 그래프 데이터
  brixComparison: [
    { name: "오렌지", brix: 8, color: "bg-orange-200" },
    { name: "수박", brix: 11, color: "bg-red-200" },
    { name: "자두", brix: 13, color: "bg-pink-200" },
    { name: "푸드지 참외", brix: 19, color: "bg-yellow-400" },
  ],

  // 포인트 1, 2
  point1: {
    title: "평균 19brix! 달콤한\n고당도 꿀 참외",
    desc: "꿀벌 수정 재배로 당도가 높을 뿐 아니라,\n신선도가 오래 유지되어 맛과 향이 우수합니다"
  },
  point2: {
    title: "참외가 가장 맛있는\n경북 성주 참외",
    desc: "성주는 참외 생산량의 70% 이상을 차지하며,\n성주 참외는 아삭한 식감과 높은 당도를 자랑합니다"
  }
};
