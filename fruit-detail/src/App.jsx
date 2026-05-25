import React from 'react';
import { productData } from './data';
import { Frown, Smile, X, Check } from 'lucide-react';

function App() {
  const { fruitName, region, brix, brandName, images, competitor, ourProduct, brixComparison, point1, point2 } = productData;

  return (
    <div className="w-full max-w-[800px] mx-auto bg-white font-sans text-center pb-20 shadow-xl min-h-screen">
      
      {/* 1. Hero Section */}
      <div className="pt-16 pb-12 px-4 flex flex-col items-center border-t-8 border-brand">
        <h2 className="text-3xl font-black text-brand mb-2 tracking-tighter bg-red-100 px-4 py-1 inline-block">
          {productData.heroSubtitle}
        </h2>
        <h1 className="text-6xl font-black text-black mb-8 leading-tight tracking-tighter whitespace-pre-line">
          {productData.heroTitle}
        </h1>
        <p className="text-xl font-bold text-gray-700 mb-2">신선도 UP, 가격 DOWN</p>
        <h3 className="text-3xl font-black text-brand mb-4 whitespace-pre-line tracking-tighter">
          {productData.heroWarning}
        </h3>
        <div className="bg-black text-white text-4xl font-black px-6 py-3 tracking-tighter inline-block shadow-lg">
          {productData.heroBrixHighlight}
        </div>
      </div>

      {/* Hero Image Section */}
      <div className="relative mb-12">
        <div className="absolute top-10 w-full flex flex-col items-center z-10 space-y-3">
          <div className="bg-black text-white font-black text-2xl px-6 py-2 border-2 border-white rounded shadow-xl">
            {region} {fruitName} 산지직송
          </div>
          <div className="bg-brand text-white font-black text-2xl px-6 py-2 border-2 border-white rounded shadow-xl">
            꿀 바른 듯 달콤한 맛
          </div>
          <div className="bg-black text-white font-black text-2xl px-6 py-2 border-2 border-white rounded shadow-xl">
            당일수확 당일배송
          </div>
        </div>
        <img src={images.hero} alt="Hero" className="w-full h-[600px] object-cover" />
      </div>

      {/* 2. Comparison Table */}
      <div className="py-12 px-4">
        <h2 className="text-4xl font-black mb-10 leading-tight tracking-tighter">
          {region} 산지직송 꿀 {fruitName}<br/>
          <span className="text-brand">타사 비교불가!</span>
        </h2>
        
        <div className="flex justify-center space-x-0 max-w-[600px] mx-auto mb-12">
          {/* 타사 상품 */}
          <div className="w-1/2 border-2 border-r-0 border-gray-300 rounded-l-xl overflow-hidden bg-gray-50 pb-8">
            <div className="bg-gray-200 py-3 font-bold text-gray-600 border-b-2 border-gray-300">{competitor.name}</div>
            <div className="py-6 flex flex-col items-center">
              <Frown size={50} className="text-gray-400 mb-4" />
              <ul className="text-left space-y-3 font-bold text-gray-500 text-lg">
                {competitor.points.map((p, i) => (
                  <li key={i} className="flex items-center"><X size={20} className="text-brand mr-2" strokeWidth={3} /> {p}</li>
                ))}
              </ul>
            </div>
          </div>
          {/* 자사 상품 */}
          <div className="w-1/2 border-4 border-brand rounded-xl overflow-hidden bg-white shadow-2xl relative z-10 -ml-1 scale-105">
            <div className="bg-white py-3 font-black text-brand text-lg border-b-2 border-gray-100 shadow-sm">{ourProduct.name}</div>
            <div className="py-6 flex flex-col items-center">
              <Smile size={50} className="text-brand mb-4" />
              <ul className="text-left space-y-3 font-bold text-black text-lg">
                {ourProduct.points.map((p, i) => (
                  <li key={i} className="flex items-center"><Check size={20} className="text-green-500 mr-2" strokeWidth={4} /> {p}</li>
                ))}
              </ul>
            </div>
          </div>
        </div>
        
        <div className="text-5xl font-black text-brand tracking-tighter mb-4">고당도 꿀 {fruitName}</div>
        <div className="bg-black text-white text-6xl font-black px-10 py-5 tracking-tighter inline-block mb-10 shadow-xl border-b-4 border-gray-800">
          직접 확인하세요!
        </div>
      </div>

      {/* Point Images 1 */}
      <img src={images.point1_1} alt="Point" className="w-full h-auto object-cover border-b-2 border-gray-100" />
      <img src={images.point1_2} alt="Point" className="w-full h-auto object-cover" />

      {/* 3. Brix Graph */}
      <div className="bg-[#fffdf7] py-20 px-4 mt-12 border-y border-gray-200">
        <h2 className="text-5xl font-black mb-6 tracking-tighter">
          <span className="text-black">{brandName}</span> <span className="text-orange-500">꿀 {fruitName} 당도</span>
        </h2>
        <p className="font-bold text-gray-700 mb-16 max-w-sm mx-auto text-lg leading-relaxed">
          {brandName} 꿀 {fruitName}는 일반 과일의 당도보다 더 높은 고당도의 꿀 {fruitName}로 더욱 달콤합니다
        </p>

        <div className="flex justify-center items-end space-x-8 h-72 mb-8 border-b-2 border-gray-300 pb-1 w-[80%] mx-auto">
          {brixComparison.map((item, index) => {
            const isHighest = item.brix === Math.max(...brixComparison.map(b => b.brix));
            const height = `${(item.brix / 25) * 100}%`;
            return (
              <div key={index} className="flex flex-col items-center justify-end h-full w-16">
                <span className="font-black mb-3 text-lg">{item.brix}Brix{isHighest && '~'}</span>
                <div 
                  className={`w-full rounded-t-full relative shadow-sm transition-all duration-500 ${isHighest ? 'bg-orange-500' : 'bg-[#fff0c7]'}`}
                  style={{ height }}
                >
                  {isHighest && <div className="absolute -bottom-8 left-1/2 transform -translate-x-1/2 w-20 h-20 bg-yellow-300 rounded-full border-4 border-white opacity-40 z-0" />}
                </div>
                <div className="mt-6 font-black z-10 text-xl relative">
                  {isHighest ? <span className="text-brand">{item.name}</span> : <span className="text-gray-700">{item.name}</span>}
                </div>
              </div>
            );
          })}
        </div>
      </div>

      {/* Point Images 2 */}
      <img src={images.point2_1} alt="Point" className="w-full h-auto object-cover mt-8" />

      {/* 4. Selling Points */}
      <div className="py-20 bg-white">
        <div className="inline-block border-2 border-orange-400 text-orange-500 font-bold px-8 py-1.5 rounded-full mb-6 tracking-widest text-sm">POINT 01</div>
        <h2 className="text-5xl font-black mb-6 text-orange-500 whitespace-pre-line tracking-tighter leading-tight">
          {point1.title}
        </h2>
        <p className="font-bold text-gray-800 whitespace-pre-line text-xl leading-relaxed mb-10">
          {point1.desc}
        </p>
        <img src={images.point2_2} alt="Point" className="w-full h-auto object-cover" />
      </div>

      <div className="py-20 bg-gray-50 border-t border-gray-200">
        <div className="inline-block border-2 border-orange-400 text-orange-500 font-bold px-8 py-1.5 rounded-full mb-6 tracking-widest text-sm">POINT 02</div>
        <h2 className="text-5xl font-black mb-6 text-orange-500 whitespace-pre-line tracking-tighter leading-tight">
          {point2.title}
        </h2>
        <p className="font-bold text-gray-800 whitespace-pre-line text-xl leading-relaxed mb-10">
          {point2.desc}
        </p>
      </div>

      {/* 5. Notice Section */}
      <div className="bg-[#f8f9fa] text-left p-10 mt-10 space-y-10 text-[15px] text-gray-800 leading-relaxed border-t-[12px] border-gray-300 max-w-[90%] mx-auto shadow-inner rounded-xl">
        
        <div>
          <h4 className="text-2xl font-black mb-4 flex items-center border-b-2 border-gray-300 pb-2">📦 주문 및 배송 안내</h4>
          <ul className="list-disc pl-5 space-y-2 text-gray-600 font-medium">
            <li><span className="font-bold text-gray-800">배송 기간:</span> 영업일 기준 평균 1~4일 소요 (주말/공휴일 제외)</li>
            <li><span className="font-bold text-gray-800">배송 마감:</span> 최상의 신선도를 위해 휴무일 전날에는 배송을 진행하지 않습니다. (휴무 이후 첫 평일순으로 안전하게 순차 발송)</li>
            <li className="text-brand font-bold">주문 취소 불가 안내: 배송 준비 중이거나 상품이 이미 출고된 경우 주문 취소가 불가능합니다.</li>
            <li><span className="font-bold text-gray-800">송장 조회:</span> 출고 당일 밤 늦게부터 확인 가능합니다.</li>
          </ul>
        </div>

        <div>
          <h4 className="text-2xl font-black mb-4 flex items-center border-b-2 border-gray-300 pb-2">🚚 배송 지역 및 배송비 안내</h4>
          <div className="bg-white p-5 rounded-lg shadow-sm border border-gray-200 space-y-4">
            <div>
              <p className="font-black text-gray-800 text-lg mb-1">[ 일반 상품 ]</p>
              <p className="text-gray-600 font-medium">전국 배송 가능 (제주도 및 도서산간 포함)</p>
            </div>
            <div>
              <p className="font-black text-brand text-lg mb-1">[ 신선 식품 ]</p>
              <p className="text-brand font-bold mb-2">❌ 제주도 및 도서산간 지역 배송 불가</p>
              <p className="text-gray-600 font-medium text-sm">배송 중 신선도 보장이 어렵고 반송 및 파손 위험이 높아 출고가 제한됩니다.</p>
            </div>
          </div>
        </div>

        <div>
          <h4 className="text-2xl font-black mb-4 flex items-center border-b-2 border-gray-300 pb-2">🔄 교환 및 반품 안내</h4>
          
          <div className="bg-red-50 p-5 rounded-lg border-2 border-red-200 mb-6">
            <p className="font-black text-brand text-lg mb-3">⚠️ 신선식품 구매 전 필독 (중요)</p>
            <p className="mb-2 text-gray-700 font-medium"><span className="font-bold text-brand">단순 변심에 의한 교환/반품 불가:</span> 신선식품은 소비기한이 짧고 온도·보관에 민감하여 한 번 출고된 상품은 재판매가 불가능합니다.</p>
            <p className="text-gray-700 font-medium"><span className="font-bold text-brand">주관적 사유 반품 불가:</span> 개인적인 기호(맛, 식감, 모양 등)나 주관적인 사유에 의한 반품은 어렵습니다. 신중한 구매 결정 부탁드립니다.</p>
          </div>
          
          <div className="mb-6">
            <p className="font-black text-blue-600 text-lg mb-2">⭕ 교환/반품이 가능한 경우 (파손/오배송/누락)</p>
            <p className="text-gray-600 font-medium leading-relaxed bg-blue-50 p-4 rounded-lg border border-blue-100">
              수령 후 24시간 이내에 <span className="font-bold text-black">[송장 사진, 포장 상태 사진, 제품 사진]</span>을 첨부하여 1:1 문의를 주시면 신속하게 처리해 드립니다. <br/>
              <span className="text-xs text-gray-500">(※ 사진 미첨부 시 처리가 불가능합니다.)</span>
            </p>
          </div>

          <div>
            <p className="font-black text-brand text-lg mb-2">❌ 교환/반품이 불가능한 경우</p>
            <p className="mb-3 text-sm text-gray-500 font-bold">상품마다 반품지 주소가 달라 자동 수거 접수는 불가합니다. 반드시 판매자에게 1:1 문의 후 접수해 주세요.</p>
            <ul className="list-disc pl-5 space-y-2 text-gray-700 font-bold bg-white p-5 rounded-lg border border-gray-200 shadow-sm">
              <li>고객 보관 중 변형/훼손/임의 폐기한 경우</li>
              <li>포장이 훼손되었거나 개봉 및 상품을 사용한 경우</li>
              <li>주소 오류 또는 수취인 정보 불일치로 인해 배송이 실패/반송된 경우 <span className="text-brand">(왕복 배송비 고객 부담)</span></li>
            </ul>
          </div>
        </div>

        <div className="pt-4">
          <h4 className="text-2xl font-black mb-4 flex items-center text-orange-500 border-b-2 border-orange-200 pb-2">⚠️ 구매 전 주의사항</h4>
          <ul className="list-disc pl-5 space-y-3 text-gray-600 font-medium">
            <li><span className="font-bold text-gray-800">크기 및 중량:</span> 생물 특성상 측정하는 사람과 위치에 따라 약간의 차이가 발생할 수 있습니다.</li>
            <li><span className="font-bold text-gray-800">색상 상이:</span> 모니터 해상도 및 환경에 따라 실제 상품과 약간의 색상 차이가 있을 수 있습니다.</li>
          </ul>
        </div>
      </div>

    </div>
  );
}

export default App;
